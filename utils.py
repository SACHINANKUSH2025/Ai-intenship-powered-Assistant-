import pypdf
from langchain_ollama import OllamaLLM


def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file.

    Args:
        pdf_file: A file-like object (e.g., from st.file_uploader) or path to a PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    try:
        pdf_reader = pypdf.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"


def get_llm(model_name="mistral"):
    """
    Returns a configured Ollama LLM instance.

    Args:
        model_name (str): The name of the model to use. Defaults to "mistral".

    Returns:
        OllamaLLM: The configured LLM instance.
    """
    return OllamaLLM(model=model_name)
