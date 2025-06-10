from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class InputSchemaProperty(BaseModel):
    """
    Represents a property within the input schema of a tool.
    """
    type: str = Field(..., description="The data type of the property (e.g., string, integer, boolean).")
    description: str = Field(..., description="A description of the property's purpose.")
    format: Optional[str] = Field(None, description="Optional format for the data type (e.g., 'email', 'date-time').")
    enum: Optional[List[str]] = Field(None, description="Optional list of allowed values for the property.")
    default: Optional[str] = Field(None, description="Optional default value.")

class InputSchema(BaseModel):
    type: str = Field("object", description="The type of the input schema (usually 'object').")
    properties: Dict[str, InputSchemaProperty] = Field(..., description="A dictionary where keys are property names and values are InputSchemaProperty objects.")
    required: Optional[List[str]] = Field(None, description="A list of required property names.")

class MCPTool(BaseModel):
    name: str = Field(..., description="Name of the MCP tool")
    description: str = Field(..., description="Description of the MCP tool")
    input_schema: InputSchema = Field(..., description="The schema for the tool's input parameters.")

class ToolList(BaseModel):
    tools: List[MCPTool] = Field(..., description='List of MCP tools provided by this MCP server')

# Create a router for this endpoint
router = APIRouter()

# Define the GET endpoint
@router.get("/mcp/tools", response_model=ToolList)
async def list_tools():
    resume_parser = MCPTool(name='parse_resume',
                            description='Extract key information from freetext resume',
                            input_schema=InputSchema(properties={"resume_text": InputSchemaProperty(type="string",
                                                                                                    description="Resume in free text",
                                                                                                    required=["resume_text"]
                                                                                                    )}))
    return ToolList(
        tools=[resume_parser]
    )
