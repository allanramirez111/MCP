from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="mcp",
    args=["run", "server.py"],
    env=None
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            resources = await session.list_resources()
            print("Resources:")
            for resource in resources:
                print(f"- {resource}")

            tools = await session.list_tools()
            print("Tools:")
            for tool in tools.tools:
                print(f"- {tool.name}")

            print("READING RESOURCE")
            content, mime_type = await session.read_resource("greeting://hello")
            print(f"Content: {content}")
            
            print("CALL TOOL")
            result = await session.call_tool("add", {"a": 1, "b": 2})
            print(f"Result: {result.content}")
                        
if __name__ == "__main__":
    import asyncio
    asyncio.run(run())