from collections import Counter


def duplicate_encode(word):
    word = word.lower()
    charCounts = Counter(word)
    return ''.join(')' if charCounts[c] > 1 else '(' for c in word)
