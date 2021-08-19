from collections import Counter


def letter_frequency(text):
    return sorted(Counter(filter(str.isalpha, text.lower())).most_common(), key=lambda t: (-t[1], t[0]))
