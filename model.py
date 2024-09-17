from transformers import T5Tokenizer, T5ForConditionalGeneration

def summarize_chunk(text, model, tokenizer, max_input_length=512):
    input_ids = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=max_input_length, truncation=True)
    summary_ids = model.generate(input_ids, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary_text

def summary(text, chunk_size=500):
    model = T5ForConditionalGeneration.from_pretrained('t5-base')
    tokenizer = T5Tokenizer.from_pretrained('t5-base')

    # Split the text into smaller chunks
    text_chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    # Summarize each chunk and combine the results
    summarized_chunks = [summarize_chunk(chunk, model, tokenizer) for chunk in text_chunks]
    full_summary = " ".join(summarized_chunks)

    return full_summary
