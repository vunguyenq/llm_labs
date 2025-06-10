from fastapi import APIRouter
from resume_parser.parser import ResumeChecklist, parse_resume

# Create a router for this endpoint
router = APIRouter()

# Define the GET endpoint
@router.get("/mcp/call/parse_resume", response_model=ResumeChecklist)
async def parse_resume_endpoint(resume_text: str):
    parsed_data = parse_resume(resume_text)
    return parsed_data
