import streamlit as st
import requests

st.title("TalentX Bot")
st.write("It is a bot that recommends career, helps to find jobs, suggests and helps to detect red flags in an internship")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Let's discuss about your career"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    url = "http://localhost:8000/ask"

    response = requests.post(url, json={"query": prompt}).json()
    with st.chat_message("ai"):
        st.markdown(response)
    st.session_state.messages.append({"role": "ai", "content": response})