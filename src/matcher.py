from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_to_jd(resume_text, jd_text):
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([jd_text, resume_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return score * 100
