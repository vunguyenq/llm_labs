from resume_parser.parser import parse_resume
from utils.logging_utils import setup_logging
from resume_parser.resume_data import sample_resume_data

if __name__ == "__main__":
    # Initialize logging
    setup_logging(console=False)
    resume_raw_data = sample_resume_data(n_samples=10)
    for i, (row_index, row) in enumerate(resume_raw_data.iterrows()):
        resume_id = row['ID']
        resume_text = row['Resume_str']
        category = row['Category']
        resume_data = parse_resume(resume_text)
        print('---------------------------------------------------------------------')
        print(f"({i+1}/{len(resume_raw_data)}) Resume ID: {resume_id}. Job category: {category}")
        print(resume_data)
