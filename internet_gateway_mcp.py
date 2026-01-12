"""
Simple MCP Internet Gateway Server
=================================

This script uses FastAPI and the `fastmcp` library to expose a remote Model
Context Protocol (MCP) server that allows GPT models to search the web and
retrieve page content.  It defines two tools:

* `search(query: str)` – runs a web search and returns a list of result
  entries.  For demonstration it uses DuckDuckGo's HTML search endpoint.  In
  production you should replace this with a proper search API (Google
  Custom Search, Bing, etc.) and handle API keys and rate limits.

* `fetch(id: str)` – treats the provided `id` as a URL, fetches the page
  content using an HTTP GET request and returns its plain text.  Only
  requests to domains on a configurable allowlist are permitted.

The server enforces a domain allowlist via the `ALLOWED_DOMAINS`
environment variable.  If you set `ALLOWED_DOMAINS` to "*" every domain is
allowed, but doing so eliminates an important safety guard; OpenAI
recommends restricting network requests to known‑good domains and to safe
HTTP methods such as `GET`, `HEAD` and `OPTIONS`【610014789420518†L248-L270】.

Usage
-----

Install the required packages:

```bash
pip install fastapi fastmcp uvicorn requests beautifulsoup4
```

Run the server locally with an allowlist of specific domains:

```bash
export ALLOWED_DOMAINS="wikipedia.org,openai.com"
uvicorn internet_gateway_mcp:app --host 0.0.0.0 --port 8000
```

Deploy to any cloud platform that can run a Python web service.  Make sure
your service is accessible over HTTPS and note its base URL for the
`server_url` parameter when registering the tool with OpenAI.

Example integration with OpenAI’s Responses API:

```python
from openai import OpenAI

client = OpenAI()
response = client.responses.create(
    model="gpt-4.1",
    tools=[{
        "type": "mcp",
        "server_label": "internet-gateway",
        "server_url": "https://gateway.example.com",
        "require_approval": "never",
    }],
    input="Search the web for the latest Houston Metro Police news",
)
print(response.output_text)
```

"""

import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, HTTPException
from fastmcp import FastMCP


# Define a default allowlist.  You should override this via the
# ALLOWED_DOMAINS environment variable or by passing "*" to allow all.
DEFAULT_ALLOWED = ["*"]

# Read allowed domains from the environment.  Split on commas and strip
# whitespace.  If nothing is provided, fall back to the default.
env_allowlist = os.getenv("ALLOWED_DOMAINS", "*").split(",")
ALLOWED_DOMAINS = [d.strip() for d in env_allowlist if d.strip()] or DEFAULT_ALLOWED


def _check_url_allowed(url: str) -> None:
    """Raise an HTTPException if the URL’s domain is not in the allowlist."""
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    # If a wildcard is present, every domain is permitted.
    if "*" in ALLOWED_DOMAINS:
        return
    # Check for exact match or subdomain match.
    for allowed in ALLOWED_DOMAINS:
        allowed = allowed.lower()
        if domain == allowed or domain.endswith("." + allowed):
            return
    raise HTTPException(status_code=403, detail=f"Domain '{domain}' not allowed")


app = FastAPI()
"""
Create a FastMCP server instance.  The instructions string describes
the server’s purpose to the model.  The FastMCP instance exposes a
`fastapi_app` property that plugs into our FastAPI application.
"""
mcp = FastMCP(name="Internet Gateway MCP",
              instructions=(
                  "This MCP server provides web search and document retrieval. "
                  "Use the search tool to look up web pages by keyword and the "
                  "fetch tool to download their text."
              ))


@mcp.tool()
async def search(query: str):
    """
    Perform a web search and return a list of results.

    Args:
        query: The search query string.

    Returns:
        A dictionary with a single key ``results`` whose value is a list of
        result objects.  Each result includes ``id`` (the URL), ``title``, and
        ``url``.  You can pass the ``id`` directly to the ``fetch`` tool to
        retrieve the full page content.  Results are filtered by the
        configured domain allowlist.
    """
    if not query or not query.strip():
        return {"results": []}

    # Use DuckDuckGo's HTML search endpoint for demonstration.  You may
    # substitute this with another search provider or your own service.
    search_url = "https://duckduckgo.com/html/"
    params = {"q": query}
    try:
        resp = requests.get(search_url, params=params,
                            headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Search request failed: {e}")

    if resp.status_code != 200:
        raise HTTPException(status_code=502,
                            detail=f"Search returned {resp.status_code}")

    soup = BeautifulSoup(resp.text, "html.parser")
    results = []
    # DuckDuckGo results are contained in elements with class 'result__title'
    for result in soup.select(".result__title")[:5]:
        anchor = result.find("a", href=True)
        if not anchor:
            continue
        url = anchor["href"]
        title = anchor.get_text(strip=True) or url
        # Skip results that point to disallowed domains
        try:
            _check_url_allowed(url)
        except HTTPException:
            continue
        results.append({"id": url, "title": title, "url": url})
    return {"results": results}


@mcp.tool()
async def fetch(id: str):
    """
    Retrieve the full text of a web page by URL.

    Args:
        id: The URL of the page to fetch.  This should be one of the
            ``id`` values returned by the ``search`` tool.

    Returns:
        A dictionary containing ``id``, ``title``, ``text``, ``url`` and
        ``metadata`` keys.  This structure conforms to the specification of
        the ``fetch`` tool described in OpenAI’s documentation【118307517586934†L274-L288】.
    """
    if not id:
        raise HTTPException(status_code=400, detail="id (URL) is required")

    url = id
    _check_url_allowed(url)
    try:
        resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Failed to fetch {url}: {e}")

    if resp.status_code != 200:
        raise HTTPException(status_code=502,
                            detail=f"Failed to fetch {url}: status {resp.status_code}")

    soup = BeautifulSoup(resp.text, "html.parser")
    title = soup.title.string.strip() if soup.title and soup.title.string else url
    text = soup.get_text(separator="\n")
    return {
        "id": url,
        "title": title,
        "text": text,
        "url": url,
        "metadata": None,
    }


# Export the FastMCP HTTP app for uvicorn
# Call http_app() method to create the Starlette application
app = mcp.http_app()