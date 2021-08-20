from collections import Counter


def letter_frequency(text):
    cnts = Counter((c for c in text.lower() if c.isalpha())).most_common()
    return sorted(cnts, key=lambda x: (-x[1], x[0]))
