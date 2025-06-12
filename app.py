import streamlit as st
import os
import tempfile
import pandas as pd
from src.matcher import match_resume_to_jd
from src.resume_parser import extract_text_from_pdf
from src.text_cleaner import preprocess

st.set_page_config(page_title="AI Resume Matcher", layout="centered")

st.title("📄 AI-Powered Resume Matcher")
st.markdown("Enter a **Job Description** below and upload **multiple resumes** to match the best candidates.")

#  JD Text Input
jd_text = st.text_area("🧾 Enter Job Description", height=200, placeholder="Paste the job description here...")

#  Upload Resumes
resumes = st.file_uploader("📎 Upload Resumes (PDFs only)", type=["pdf"], accept_multiple_files=True)

#  Trigger Matching
if jd_text and resumes:
    jd_clean = preprocess(jd_text)
    scores = []

    for resume in resumes:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(resume.read())
            tmp_path = tmp.name

        resume_text = extract_text_from_pdf(tmp_path)
        resume_clean = preprocess(resume_text)
        score = match_resume_to_jd(resume_clean, jd_clean)

        scores.append({
            "Resume File": resume.name,
            "Match Score (%)": round(score, 2)
        })

    sorted_scores = sorted(scores, key=lambda x: x["Match Score (%)"], reverse=True)

    st.success("✅ Matching Completed")
    st.dataframe(pd.DataFrame(sorted_scores))

else:
    st.info("Please provide a job description and upload at least one resume.")
