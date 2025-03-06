import streamlit as st
import random
import string
import re

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "@$!%*?&"
    return ''.join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.search(r"[@$!%*?&]", password))
    
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    
    if criteria_met == 5:
        return "🟢 Strong"
    elif criteria_met >= 3:
        return "🟠 Medium"
    else:
        return "🔴 Weak"

def main():
    st.set_page_config(page_title="🔐 Password Strength Checker & Generator", page_icon="🔒")
    st.markdown(
        """
        <style>
        .main-container {text-align: center;}
        .stTextInput input {border-radius: 10px; padding: 10px; font-size: 16px; text-align: center;}
        .stButton button {border-radius: 10px; background-color: #007BFF; color: white; padding: 12px 24px; width: 100%; font-size: 16px; font-weight: bold;}
        .stButton button:hover {background-color: #0056b3;}
        h1, h2, h3, h4, h5 {text-align: center;}
        .watermark {position: fixed; bottom: 10px; right: 20px; opacity: 0.5; font-size: 14px;}
        </style>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown("<h1>🔐 Password Strength Checker & Generator</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Check how strong your password is and generate a secure password instantly.</h3>", unsafe_allow_html=True)
    
    password = st.text_input("Enter Password", type="password")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Check Strength"):
            if password:
                strength = check_password_strength(password)
                st.success(f"Password Strength: {strength}")
            else:
                st.warning("Please enter a password to check.")
    
    st.markdown("---")
    st.markdown("<h2>🔑 Need a Secure Password?</h2>", unsafe_allow_html=True)
    
    with col2:
        if st.button("Generate Strong Password"):
            new_password = generate_password()
            st.text_input("Generated Password", new_password, disabled=True)
    
    st.markdown("<div class='watermark'>Made by Mustafa Khan</div>", unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
