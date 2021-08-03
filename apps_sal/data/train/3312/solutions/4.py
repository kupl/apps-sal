from collections import Counter
from itertools import combinations


def anagram_counter(words):
    return sum(1 for a, b in combinations((frozenset(Counter(w)) for w in words), 2) if a == b)
