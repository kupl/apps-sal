# return a list of tuples sorted by frequency with
# the most frequent letter first. Any letters with the
# same frequency are ordered alphabetically

def letter_frequency(text):
    text = text.lower()
    freq = sorted([(l, text.count(l)) for l in set(text) if l.isalpha()], key=lambda k: k[0])
    return sorted(freq, key=lambda k: k[1], reverse=True)
