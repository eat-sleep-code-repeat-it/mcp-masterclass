from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")
@mcp.tool()
def get_weather(location: str) -> str:
    """
    Get the current weather for a given location.
    
    Args:
        location (str): The name of the location to get the weather for.
    
    Returns:
        str: A string describing the current weather in the specified location.
    """
    # This is a placeholder implementation. In a real application, you would
    # fetch the weather data from an API or database.
    return f"The current weather in {location} is sunny with a temperature of 25°C."

if __name__ == "__main__":
    mcp.run()
