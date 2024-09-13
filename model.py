from transformers import PegasusForConditionalGeneration, PegasusTokenizer, pipeline

# Load the tokenizer and model
model_name = "google/pegasus-xsum"
pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)
pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)

# Define function for decoding summary (title summary)
def title_summary(text):
    """
    Generates a short summary (title-like) from the input text.
    """
    # Tokenize and create input for the model
    tokens = pegasus_tokenizer(text, truncation=True, padding="longest", return_tensors="pt")

    # Generate a short summary
    encoded_summary = pegasus_model.generate(**tokens)

    # Decode the summarized text and return it
    decoded_summary = pegasus_tokenizer.decode(encoded_summary[0], skip_special_tokens=True)
    return decoded_summary

# Define function for longer summary
def detailed_summary(text, min_length=30, max_length=150):
    """
    Generates a more detailed summary of the input text.
    """
    summarizer = pipeline(
        "summarization",
        model=pegasus_model,
        tokenizer=pegasus_tokenizer,
        framework="pt"
    )

    # Generate the summary with length constraints
    summary = summarizer(text, min_length=min_length, max_length=max_length)

    # Extract and return the summarized text
    return summary[0]["summary_text"]
