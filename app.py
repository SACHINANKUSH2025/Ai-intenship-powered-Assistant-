import streamlit as st
from auth import auth_page
from resume_feedback import resume_feedback
from cover_letter import generate_cover_letter
from mock_interview import mock_interview
from skill_gap import skill_gap_analysis

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Internship Assistant",
    layout="centered"
)
# Session init
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 🔒 Login Gate
if not st.session_state.logged_in:
    st.title("🎓 AI-Powered Internship Assistant")
    auth_page()
    st.stop()

# ✅ After Login
st.sidebar.success(f"Welcome {st.session_state.user}")

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

st.markdown("""
<style>

/* Google Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

/* Global */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Main background */
.stApp {
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(12px);
    border-right: 1px solid rgba(255,255,255,0.2);
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: white;
}

/* Title */
h1 {
    font-size: 2.6rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 0.2em;
}

h2, h3 {
    font-weight: 600;
}

/* Card-style containers */
.css-1r6slb0, .css-12w0qpk {
    background: rgba(255,255,255,0.18);
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
    backdrop-filter: blur(10px);
}

/* File uploader */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.18);
    border-radius: 12px;
    padding: 15px;
}

/* Inputs */
input, textarea {
    border-radius: 10px !important;
    border: none !important;
    padding: 10px !important;
    font-size: 15px !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 12px;
    padding: 0.7em 1.6em;
    font-size: 16px;
    font-weight: 600;
    border: none;
    transition: all 0.3s ease-in-out;
    box-shadow: 0 6px 15px rgba(0,0,0,0.25);
}

/* Button hover */
.stButton > button:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 10px 25px rgba(0,0,0,0.35);
}

/* Labels */
label {
    font-weight: 500;
    color: #f1f5f9 !important;
}

/* JSON output */
pre {
    background: rgba(0,0,0,0.35) !important;
    border-radius: 12px;
    padding: 15px;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: linear-gradient(#00c6ff, #0072ff);
    border-radius: 10px;
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
st.sidebar.markdown("### 👨‍💻 Meet Our Developers")
st.sidebar.markdown("""
  
**Team Members:** 
- Sachin Ankush
- Aditya Nagargoje  
- Krishna Patil  
- Kamna Wagh
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


