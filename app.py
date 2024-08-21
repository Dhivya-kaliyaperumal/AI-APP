import streamlit as st 
import google.generativeai as genai


st.title("Welcome to AI chat")


genai.configure(api_key="AIzaSyA9sNijjq8I4CkaXZw8xXix6Ib7J_LAuaE")

text = st.text_input("enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])



if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)