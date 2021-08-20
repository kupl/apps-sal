def letter_frequency(text):
    text = text.lower()
    freq = sorted([(l, text.count(l)) for l in set(text) if l.isalpha()], key=lambda k: k[0])
    return sorted(freq, key=lambda k: k[1], reverse=True)
