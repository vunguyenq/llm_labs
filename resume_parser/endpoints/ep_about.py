from fastapi import APIRouter
from resume_parser.parser import ResumeChecklist, parse_resume
from pydantic import BaseModel, Field


class APIInfo(BaseModel):
    api_description: str = Field(..., description="Description of the API")
    api_version: str = Field(..., description="Version of the API")

# Create a router for this endpoint
router = APIRouter()

# Define the GET endpoint
@router.get("/about", response_model=APIInfo)
async def parse_resume_endpoint():
    return APIInfo(
        api_description="This API provides functionality to parse resumes and extract structured information.",
        api_version="1.0.0"
    )
