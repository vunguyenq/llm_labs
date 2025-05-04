import pandas as pd

def sample_resume_data(n_samples: int = 1, fields: list[str] = None) -> dict:
    """
    Sample resume data from the resume database.
    """
    if not fields:
        fields = ['ID', 'Resume_str', 'Category']  # Ignore Resume_html by default
    resume_db = pd.read_csv('resume_parser/raw_data/Resume.csv', usecols=fields)
    return resume_db.sample(n_samples)
