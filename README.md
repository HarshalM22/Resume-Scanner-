# AI-Powered Resume Matcher

A simple NLP-based app that compares a resume PDF to a job description and gives a match score using TF-IDF and cosine similarity.

## Features
- Extracts text from PDF resumes
- Cleans and tokenizes text
- Calculates similarity with job description
- Streamlit UI for demo

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Folder Structure
```
resume-scanner/
├── resumes/                 # Place sample resume PDFs here
├── job_descriptions/        # Place job descriptions here
├── src/
│   ├── resume_parser.py
│   ├── text_cleaner.py
│   └── matcher.py
├── app.py
└── README.md
