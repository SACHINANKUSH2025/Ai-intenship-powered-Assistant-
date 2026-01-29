import streamlit as st
import sqlite3
import hashlib

# ---------- DB SETUP ----------
def get_db():
    conn = sqlite3.connect("users.db")
    return conn

def create_users_table():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

# ---------- SECURITY ----------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---------- AUTH FUNCTIONS ----------
def signup():
    st.subheader("📝 Sign Up")

    username = st.text_input("Create Username")
    password = st.text_input("Create Password", type="password")

    if st.button("Register"):
        if not username or not password:
            st.warning("All fields required ⚠️")
            return

        conn = get_db()
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hash_password(password))
            )
            conn.commit()
            st.success("Account created! Please login ✅")
        except sqlite3.IntegrityError:
            st.error("Username already exists ❌")
        finally:
            conn.close()

def login():
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, hash_password(password))
        )
        user = cur.fetchone()
        conn.close()

        if user:
            st.session_state.logged_in = True
            st.session_state.user = username
            st.success("Login successful ✅")
            st.rerun()
        else:
            st.error("Invalid credentials ❌")

# ---------- MAIN AUTH PAGE ----------
def auth_page():
    create_users_table()

    # ---------- Background CSS ----------
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #00c6ff, #0072ff);
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- UI ----------#
    choice = st.radio("Choose Option", ["Login", "Sign Up"])

    if choice == "Login":
        login()
    else:
        signup()





