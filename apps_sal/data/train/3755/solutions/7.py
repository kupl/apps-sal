def sortme(words):
    return sorted(words, key=lambda w: (w.upper(), w[0].islower()))
