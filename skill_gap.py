import spacy
from utils import extract_text_from_pdf

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    doc = nlp(text)
    skills = set()
    for token in doc:
        if token.pos_ == "NOUN":
            skills.add(token.text.lower())
    return skills

def skill_gap_analysis(pdf, job_desc):
    resume_text = extract_text_from_pdf(pdf)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)

    missing_skills = job_skills - resume_skills

    return {
        "Resume Skills": list(resume_skills),
        "Required Skills": list(job_skills),
        "Missing Skills": list(missing_skills)
    }
