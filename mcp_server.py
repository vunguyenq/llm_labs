'''This is the main entry point for the Resume Parser API.
It initializes the FastAPI application and includes the routers for the API endpoints.
'''
from fastapi import FastAPI
from resume_parser.endpoints import ep_parse_resume, ep_tools
from utils.logging_utils import setup_logging
import uvicorn

# Create FastAPI app
app = FastAPI(title="MCP API", description="API providing tools to parse resumes from raw text", version="1.0.0")

# Include routers from endpoint modules
app.include_router(ep_tools.router)  # http://localhost:8000/mcp/tools
app.include_router(ep_parse_resume.router, tags=["Resume"])  # http://localhost:8000/mcp/call/parse_resume?resume_text=Jane%20Doe%20software%20engineer

# To run the app: uvicorn app.main:app --reload
if __name__ == "__main__":
    setup_logging(console=False)
    uvicorn.run(app, host="0.0.0.0", port=8000)