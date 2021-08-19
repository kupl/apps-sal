from collections import Counter


def word_square(letters):
    sq = len(letters) ** 0.5
    if sq % 1 != 0:
        return False
    d = Counter(letters)
    return len([True for c in d if d[c] % 2 == 1]) <= sq
