import streamlit as st
from resume_feedback import resume_feedback
from cover_letter import generate_cover_letter
from mock_interview import mock_interview
from skill_gap import skill_gap_analysis

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Internship Assistant",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
/* Main background */
.stApp {
    background-color: #87CEEB; /* Sky Blue */
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #5dade2; /* Darker sky blue */
    color: white;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: white;
}

/* Buttons */
.stButton > button {
    background-color: white;
    color: #1f2937;
    border-radius: 10px;
    padding: 0.6em 1.2em;
    font-size: 16px;
    font-weight: bold;
    transition: all 0.3s ease;
}

/* Button hover */
.stButton > button:hover {
    background-color: #2563eb;
    color: white;
    transform: scale(1.05);
}

/* Inputs & text areas */
input, textarea {
    border-radius: 8px !important;
    color: black !important;
}

/* Labels */
label {
    color: white !important;
}

/* Headings */
h1, h2, h3 {
    color: white;
}
</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------
st.title("🎓 AI-Powered Internship Assistant")
st.write("Your smart companion for resumes, interviews, and skill growth 🚀")

# ---------------- SIDEBAR MENU ----------------
menu = st.sidebar.selectbox(
    "Choose Feature",
    ["Resume Feedback", "Cover Letter Generator", "Mock Interview", "Skill Gap Analysis"]
)

st.sidebar.markdown("---")

# ---------------- TEAM INFO ----------------
st.sidebar.markdown("### 👥 Project Team")
st.sidebar.markdown("""
  
**Team Members:** 
- Sachin Ankush  
- Krishana Patil  
- Kamna Wagh
- Aditya Nagargoje 
- Aniket Mundhe 
""")

# ---------------- INPUTS ----------------
resume = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("📝 Paste Job Description")

# ---------------- FEATURES ----------------
if menu == "Resume Feedback" and resume:
    if st.button("🔍 Analyze Resume"):
        st.write(resume_feedback(resume, job_desc))

elif menu == "Cover Letter Generator" and resume:
    if st.button("✉️ Generate Cover Letter"):
        st.write(generate_cover_letter(resume, job_desc))

elif menu == "Mock Interview":
    role = st.text_input("🎯 Enter Target Role")
    if st.button("🎤 Start Interview"):
        mock_interview(role)

elif menu == "Skill Gap Analysis" and resume:
    if st.button("📊 Analyze Skills"):
        result = skill_gap_analysis(resume, job_desc)
        st.json(result)
