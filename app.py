import streamlit as st
from src.resume_parser import extract_resume_text
from src.text_cleaner import preprocess
from src.matcher import compute_match_score

st.title("🔍 AI-Powered Resume Matcher")

jd = st.text_area("Enter Job Description:")
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if st.button("Match"):
    if resume_file and jd:
        with open("temp_resume.pdf", "wb") as f:
            f.write(resume_file.read())
        resume_text = extract_resume_text("temp_resume.pdf")
        resume_clean = preprocess(resume_text)
        jd_clean = preprocess(jd)

        score = compute_match_score(resume_clean, jd_clean)
        st.success(f"\n\nMatch Score: {score:.2f}%")
    else:
        st.warning("Please upload a resume and enter job description.")