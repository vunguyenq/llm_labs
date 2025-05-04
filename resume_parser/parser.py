from openai import AzureOpenAI
from pydantic import BaseModel, Field
from typing import List, Optional
from env import config
import logging


class ResumeChecklist(BaseModel):
    first_name: str = Field(..., description="Candidate's first name")
    second_name: str = Field(..., description="Candidate's second name or family name")
    skills: List[str] = Field(..., description="Technical or professional skills listed")
    experience_years: int = Field(..., description="Total number of years of professional experience")
    education_level: str = Field(..., description="Highest education level attained (e.g. Bachelor's, Master's, PhD)")
    last_job_role: str = Field(..., description="Most recent or current job title mentioned in resume")
    salary_expectation: Optional[int] = Field(None, description="Salary expectation if explicitly mentioned (annual, USD)")
    projects_count: Optional[int] = Field(None, description="Number of distinct projects mentioned or led in resume")


def parse_resume(resume_text: str) -> ResumeChecklist:
    """
    Parses the resume text and extracts relevant information into a structured format.
    """
    client = AzureOpenAI(api_key=config.AZURE_OPENAI_API_KEY,
                         api_version=config.AZURE_OPENAI_API_VERSION,
                         azure_endpoint=config.AZURE_OPENAI_ENDPOINT)

    messages = [
        {
            "role": "system",
            "content": "You are a recruiting assistant. You help Human Resource department scan candidates' resume in free text and extract structured details."
        },
        {
            "role": "user",
            "content": resume_text
        }
    ]

    logging.info(f"MESSAGE_SENT: {messages}")

    response = client.beta.chat.completions.parse(
        model=config.AZURE_OPENAI_DEPLOYMENT,
        messages=messages,
        response_format=ResumeChecklist
    )

    logging.info(f"RESPONSE_RECEIVED: {response.model_dump()}")

    return response.choices[0].message.parsed
