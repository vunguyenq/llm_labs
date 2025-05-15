import os
import openai
from agents import Agent, Runner
from agents.mcp.server import MCPServerSse, MCPServerSseParams
import asyncio

# Configure Azure OpenAI credentials
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_version = "2023-03-15-preview"  # or the appropriate API version for your model

# Set up MCP server client pointing to our FastAPI server
tools_server = MCPServerSse(params=MCPServerSseParams(url="http://localhost:8000/mcp", name='MCP server'))

agent = Agent(
    name="HR Assistant",
    model="gpt-4",  # might be configured internally to use Azure via openai library
    instructions="You are an HR assistant that analyzes resumes. You have a tool to parse resumes for details.",
    mcp_servers=[tools_server]
)

prompt = 'List the tools you have and describe them.'
result = Runner.run_sync(agent, prompt)
print(result.final_output)