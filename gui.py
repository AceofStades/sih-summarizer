import streamlit as st
import time
from model import summary

st.file_uploader("Upload your document:", type=["pdf", "docx", "doc"], accept_multiple_files=False, key="doc", help=None)
text = st.text_area(label = "Enter your text to summarize", max_chars=2000, placeholder="Max characters: 2000", height=400)

def typewriter(text: str, speed=10):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text)
        time.sleep(1 / speed)

if st.button("Summarize"):
	with st.spinner('Wait for it... (This may take some time)'):
		summarized = summary(text)
	typewriter("Summary: " + summarized)
