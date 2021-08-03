from collections import Counter


def letter_frequency(text):
    return sorted(Counter(''.join([c for c in text.lower() if c.isalpha()])).items(), key=lambda x: (-x[1], x[0]))
