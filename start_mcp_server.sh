#!/bin/bash
# MCP Internet Gateway Server Startup Script
# This allows unrestricted internet access for GPT agents

# Allow ALL domains (remove internet restrictions)
export ALLOWED_DOMAINS="*"

# Start the server
echo "========================================"
echo " MCP Internet Gateway Server"
echo "========================================"
echo "✅ Allowing access to ALL domains"
echo "🌐 Server: http://0.0.0.0:8000"
echo "🔧 MCP Endpoint: http://localhost:8000/mcp"
echo ""
echo "Press CTRL+C to stop the server"
echo "========================================"
echo ""

cd "$(dirname "$0")"
python3 -m uvicorn internet_gateway_mcp:app --host 0.0.0.0 --port 8000 --reload
