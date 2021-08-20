def capitals_first(text):
    words = [w for w in text.split() if w[0].isalpha() and (not w.isnumeric())]
    return ' '.join(sorted(words, key=lambda w: w[0] != w[0].upper()))
