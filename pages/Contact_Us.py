import streamlit as st
from send_email import send_email

st.header("Contact me ")

with st.form(clear_on_submit=True, key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")

    # Use backslash, blank rule and no indentations for correct format message
    message = f"""\
Subject: New mail from {user_email} 
    
From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button and message != "":
        send_email(message)
        st.info("Your mail has been sent.")
