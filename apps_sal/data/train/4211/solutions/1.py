from collections import Counter


def validate_word(word):
    return 1 == len(set(Counter(word.upper()).values()))
