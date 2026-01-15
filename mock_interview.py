import streamlit as st
from langchain_community.llms import Ollama

def mock_interview(role, llm):
    question = llm(f"Ask one interview question for a {role} intern.")
    return question
    st.subheader("Interview Question")
    st.write(question)

    answer = st.text_area("Your Answer")

    if st.button("Get Feedback"):
        feedback = llm(f"""
        Question: {question}
        Answer: {answer}
        Provide feedback and tips.
        """)
        st.subheader("Feedback")
        st.write(feedback)
