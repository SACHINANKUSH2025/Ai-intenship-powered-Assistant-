import streamlit as st
from langchain_community.llms import Ollama

llm = Ollama(model="mistral")

def mock_interview(role):
    question = llm.invoke(f"Ask a technical interview question for a {role} intern.")
    st.write("### Interview Question:")
    st.write(question)

    answer = st.text_area("Your Answer")

    if st.button("Get Feedback"):
        feedback = llm(f"""
        Question: {question}
        Answer: {answer}
        Give feedback and improvement tips.
        """)
        st.write("### Feedback:")
        st.write(feedback)