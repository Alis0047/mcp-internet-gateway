# MCP Internet Gateway

An MCP (Model Context Protocol) server that provides unrestricted internet access for AI agents. Allows GPT and other AI models to search the web and fetch content from any website.

## Features

- 🌐 **Unrestricted Internet Access** - Access any domain on the internet
- 🔍 **Web Search** - Search the web using DuckDuckGo
- 📄 **Content Fetching** - Retrieve and parse content from any URL
- 🚀 **Easy Deployment** - Deploy to any cloud platform
- 🔧 **MCP Protocol** - Full Model Context Protocol support

## Quick Start

### Local Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the server:
```bash
./start_mcp_server.sh
```

Or manually:
```bash
export ALLOWED_DOMAINS="*"
uvicorn internet_gateway_mcp:app --host 0.0.0.0 --port 8000
```

The server will be available at `http://localhost:8000/mcp`

## Deploy to Cloud

### Render.com (Recommended - Free)

1. Fork/clone this repo
2. Go to https://render.com
3. New Web Service → Connect your repo
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn internet_gateway_mcp:app --host 0.0.0.0 --port $PORT`
   - **Environment Variable**: `ALLOWED_DOMAINS=*`
5. Deploy!

### Railway.app

1. Go to https://railway.app
2. New Project → Deploy from GitHub
3. Add environment variable: `ALLOWED_DOMAINS=*`
4. Deploy automatically

### Fly.io

```bash
flyctl launch
flyctl secrets set ALLOWED_DOMAINS="*"
flyctl deploy
```

## Usage with AI Agents

### OpenAI GPT

```python
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Search the web for latest AI news"}],
    tools=[{
        "type": "mcp",
        "server_label": "internet-gateway",
        "server_url": "https://your-deployed-url.com",
        "require_approval": "never",
    }]
)
```

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "internet": {
      "command": "/path/to/start_mcp_server.sh"
    }
  }
}
```

## Available Tools

### search(query: str)
Search the web and return results with URLs and titles.

**Example:**
```json
{
  "query": "latest AI developments"
}
```

### fetch(id: str)
Fetch and parse content from a URL.

**Example:**
```json
{
  "id": "https://example.com/article"
}
```

## Configuration

Control allowed domains via the `ALLOWED_DOMAINS` environment variable:

- `*` - Allow all domains (default)
- `wikipedia.org,github.com` - Specific domains only

## Security

⚠️ **Important**: The default configuration (`ALLOWED_DOMAINS="*"`) allows access to ANY website. For production use with untrusted agents, consider:

1. Restricting to specific domains
2. Adding authentication
3. Rate limiting
4. Request logging

## License

MIT License - feel free to use and modify as needed.

## Contributing

Pull requests welcome! Please open an issue first to discuss proposed changes.
