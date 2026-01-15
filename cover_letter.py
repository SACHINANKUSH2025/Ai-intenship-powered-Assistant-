from langchain_ollama import OllamaLLM
from utils import extract_text_from_pdf

# Correct instantiation
llm = OllamaLLM(model="mistral")

def generate_cover_letter(pdf, job_desc):
    resume_text = extract_text_from_pdf(pdf)

    prompt = f"""
    Write a professional cover letter using the resume and job description.

    Resume:
    {resume_text}

    Job Description:
    {job_desc}
    """

    # Use .invoke() instead of calling directly
    return llm.invoke(prompt)