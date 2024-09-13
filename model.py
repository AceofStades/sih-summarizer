from transformers import BartTokenizer, BartModel

tokenizer = BartTokenizer.from_pretrained('facebook/bart-base')
model = BartModel.from_pretrained('facebook/bart-base')

# Define function for decoding summary (title summary)
def title_summary(text):
    """
    Generates a short summary (title-like) from the input text.
    """
    # Tokenize and create input for the model
    tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")

    # Generate a short summary
    encoded_summary = model.generate(**tokens)

    # Decode the summarized text and return it
    decoded_summary = tokenizer.decode(encoded_summary[0], skip_special_tokens=True)
    return decoded_summary

# Define function for longer summary
def detailed_summary(text, min_length=30, max_length=150):
    """
    Generates a more detailed summary of the input text.
    """
    summarizer = pipeline(
        "summarization",
        model=model,
        tokenizer=tokenizer,
        framework="pt"
    )

    # Generate the summary with length constraints
    summary = summarizer(text, min_length=min_length, max_length=max_length)

    # Extract and return the summarized text
    return summary[0]["summary_text"]
