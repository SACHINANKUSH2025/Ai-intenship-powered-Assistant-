from langchain_ollama import OllamaLLM
from utils import extract_text_from_pdf

# Initialize Ollama LLM
llm = OllamaLLM(model="mistral")

def resume_feedback(pdf, job_desc):
    resume_text = extract_text_from_pdf(pdf)

    prompt = f"""
    Analyze the resume for the job description.

    Give:
    1. Strengths
    2. Weaknesses
    3. Improvement suggestions

    Resume:
    {resume_text}

    Job Description:
    {job_desc}
    """


    return llm.invoke(prompt)
