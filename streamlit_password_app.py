import streamlit as st
import random
import string

st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")


LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>?/|"


def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    pool = ""
    if use_lower:
        pool += LOWER
    if use_upper:
        pool += UPPER
    if use_digits:
        pool += DIGITS
    if use_symbols:
        pool += SYMBOLS

    if not pool:
        return "Error: Select at least one option."

    return "".join(random.choice(pool) for _ in range(length))


def strength(password):
    score = 0

    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in SYMBOLS for c in password): score += 1
    if len(password) >= 12: score += 1

    levels = {
        1: "Very Weak ❌",
        2: "Weak ⚠️",
        3: "Medium 🟡",
        4: "Strong 🟢",
        5: "Very Strong 🔥"
    }
    return levels.get(score, "Unknown")


st.title(" Password Generator (Web)")
st.write("Create strong and secure passwords instantly.")

st.subheader("Settings")

length = st.slider("Password length", 4, 40, 12)
lower = st.checkbox("Lowercase (a-z)", True)
upper = st.checkbox("Uppercase (A-Z)", True)
digits = st.checkbox("Numbers (0-9)", True)
symbols = st.checkbox("Symbols (!@#$)", True)

if st.button("Generate Password"):
    pwd = generate_password(length, lower, upper, digits, symbols)
    st.code(pwd, language="")

    st.write("**Strength:**", strength(pwd))

    st.button("Copy to Clipboard", on_click=lambda: st.session_state.update({"copy": pwd}))

if "copy" in st.session_state:
    st.write(" Password copied!")