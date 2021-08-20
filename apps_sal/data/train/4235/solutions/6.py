def make_sentences(parts):
    import re
    sentence = re.sub('\\b ([.,])', '\\1', ' '.join(parts)).rstrip('. ')
    return sentence + '.'
