from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback

server_params = StdioServerParameters(
    command = "uv",
    args=["run", "weather.py"],
)

async def run():
    try:
        print("Starting MCP client...")
        # Create a session with the server parameters
        async with stdio_client(server_params) as (reader, writer):
            print("Connected to MCP server.")
            async with ClientSession(reader, writer) as session:
                print("Initializing session...")
                await session.initialize()

                print("Listing tools...")                
                tools = await session.list_tools()
                print("Available tools:", tools)

                print("Calling tool ...")
                # Example of receiving a message from the server
                response = await session.call_tool("get_weather", arguments={"location": "New York"})   

                print("Tool response:", response)
    except Exception as e:
        print("An error occurred:", e)
        traceback.print_exc()
    
if __name__ == "__main__":
    asyncio.run(run())