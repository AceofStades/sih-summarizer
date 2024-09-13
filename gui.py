import streamlit as st
import time
from model import title_summary, detailed_summary

st.file_uploader("Upload your document:", type=["pdf", "docx", "doc"], accept_multiple_files=False, key="doc", help=None)
text = st.text_area(label = "Enter your text to summarize", max_chars=2000, placeholder="Max characters: 2000", height=400)
title = title_summary(text)
detailed = detailed_summary(text)

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
typewriter("Title:" + title, speed=speed)
typewriter("Summary:" + detailed, speed=speed)
