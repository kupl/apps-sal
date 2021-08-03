from collections import Counter


def validate_word(word):
    count = Counter(word.lower())

    return len(set(count.values())) == 1
