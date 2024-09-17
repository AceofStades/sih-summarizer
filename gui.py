import streamlit as st
import time
from model import summary
from textExtract import extract_text

def typewriter(text: str, speed=10):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text)
        time.sleep(1 / speed)

def summarize_button(text):
	if st.button("Summarize"):
		with st.spinner('Wait for it... (This may take some time)'):
			summarized = summary(text)
		typewriter("Summary: " + summarized)

uploaded_file = st.file_uploader("Upload your document:", type=["pdf"], accept_multiple_files=False, key="doc", help=None)
if uploaded_file is not None:
	text = extract_text(uploaded_file)
	summarize_button(text)

uploaded_text = st.text_area(label = "Enter your text to summarize", max_chars=10000, placeholder="Max characters: 10000", height=400)
if uploaded_text is not "":
	summarize_button(uploaded_text)


# if st.button("Summarize"):
# 	with st.spinner('Wait for it... (This may take some time)'):
# 		summarized = summary(text)
# 	typewriter("Summary: " + summarized)
