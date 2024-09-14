from summarizer import Summarizer

def summary(text):
	model = Summarizer()
	result = model(text, ratio = 0.3)
	full = ''.join(result)
	return full
