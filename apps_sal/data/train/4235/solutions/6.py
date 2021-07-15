def make_sentences(parts):
    import re
    sentence = re.sub(r'\b ([.,])', r'\1', ' '.join(parts)).rstrip('. ')
    return sentence + '.'
