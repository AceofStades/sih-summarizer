from summarizer.sbert import SBertSummarizer

def summary(text):
	model = SBertSummarizer('all-mpnet-base-v2')
	result = model(text, ratio = 0.3)
	full = ''.join(result)
	return full
