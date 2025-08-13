from mcp.server.fastmcp import FastMCP

# Crear el servidor
mcp = FastMCP("Demo")

# Tools
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def sub(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def mul(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def div(a: int, b: int) -> int:
    """Divide two numbers"""
    return a / b

@mcp.tool()
def pow(a: int, b: int) -> int:
    """Raise a number to the power of another number"""
    return a ** b

# Resource
@mcp.resource("Greeting://{name}")
def greeting(name: str) -> str:
    """Return a greeting"""
    return f"Hello {name}"
