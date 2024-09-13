import streamlit as st
import time

st.file_uploader("Upload your document:", type=["pdf", "docx", "doc"], accept_multiple_files=False, key="doc", help=None)

def typewriter(text: str, speed: int):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text)
        time.sleep(1 / speed)

#Sample Example
text = "This is an example of streamlit text with typewriter effect :)"
speed = 10
typewriter(text=text, speed=speed)
