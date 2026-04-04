import streamlit as st
import json

st.set_page_config(page_title="Login", layout="centered")

with open("users.json") as f:
    users = json.load(f)

st.title("🔐 Login System")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username in users and users[username] == password:
        st.success("Login Successful ✅")
        st.session_state["login"] = True
    else:
        st.error("Invalid Credentials ❌")

if st.session_state.get("login"):
    st.info("Sidebar → Pages open karo")