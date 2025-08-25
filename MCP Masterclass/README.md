# agentic-ai courses

## Udemy: The Complete AI Coding Course (2025) - Cursor, Claude Code
full-stack application with AI (Cursor AI, Claude Code, v0, ChatGPT, Replit) - Vibe Coding Course

## Udemy: MCP Masterclass: Complete Guide to MCP in Python [2025]

### Section 3: MSP Environment Setup
#### Tools
- VS Code - done
- copilot - done
- python - done
- claude code desktop
- npm and uv
```bash
     powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
     C:\Users\eatsl\.local\bin
```     
- openai account

### Section 4: MSP Quickstart
- https://github.com/modelcontextprotocol/python-sdk/tree/main/src/mcp/server
- https://github.com/openbnb-org/mcp-server-airbnb
- calude code -> airbnd MCP
#### Create a simple MCP Server
- vs code IDE
- make sure python and uv are installed
- don't do it in onedrive
```bash
python --version
uv --version
```
- create helloworld MCP
```bash
mkdir helloworld
uv init
uv venv
.\.venv\Scripts\activate
# install dependencies
uv add mcp[cli]

# activate mcp
.\.venv\Scripts\activate

# test mcp
mcp dev weather.py

# run mcp server locally
uv run weather.py
```
- connect to the helloworld MCP with claude
- manually add mcp to claude_desktop_config
```json
{
    "mcpServers": {
      "airbnb": {
        "command": "npx",
        "args": [
          "-y",
          "@openbnb/mcp-server-airbnb",
          "--ignore-robots-txt"
        ]
      }
    }
  }
  {
    "mcpServers": {
      "weather": {
        "command": "uv",
        "args": [
          "--directory",
          "C:\\workspace\\helloworld",
          "run",
          "weather.py"
        ]
      }
    }
  }
  ```
- install mcp
```bash
mcp install weather.py
```

#### connect an MCP Client to an MCP Server locally built
client.py point to weather MCP
#### connect an MCP Client to an MCP Server using npx
client.py point to airbnb MCP

### Section 5: MCP Server Deep Dive-Tools



### Section 6: MCP Server Deep Dive-Resources and Prompts
### Section 7: MCP Server Deep Dive-Deployment and Publishing
### Section 8: MCP Server Deep Dive-STDIO vs. Streamable HTTP
### Section 9: MCP Client Deep Dive
### Section 10: MCP End-to-End Builds
### Section 11: MCP Conclusion and Certificate
### Section 12: Bonus
### reference
- https://github.com/modelcontextprotocol/python-sdk/tree/main/src/mcp/server