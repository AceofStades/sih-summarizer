from summarizer.sbert import SBertSummarizer

def summary(text):
	model = SBertSummarizer('t5-base')
	result = model(text, ratio = 0.3)
	full = ''.join(result)
	return full
