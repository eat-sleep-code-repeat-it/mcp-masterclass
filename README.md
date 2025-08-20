# MCP

```bash
uv init mcp-masterclass
cd mcp-masterclass
git init
git branch -m master main
git remote add origin https://github.com/eat-sleep-code-repeat-it/mcp-masterclass.git
uv venv
.venv\Scripts\activate
uv add mcp[cli]
mcp dev weather.py
# claude -> settings -> Developer -> Edit Config
tasklist | findstr /i claude
taskkill /F /IM claude.exe
```

## edit claude_desktop_config.json
```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\workspace\\mcp-masterclass",
        "run",
        "weather.py"          
      ]
    }
  }
}
```

## Or Install and automatically add it to Claude
```bash
mcp install weather.py
```
## Connect an MCP Client to an MCP Server locally

```bash
uv run client.py
```
## connect an MCP client to an MCP Server using NPX
```bash
uv run client_npx.py
```


