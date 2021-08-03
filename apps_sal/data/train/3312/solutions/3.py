from collections import Counter


def anagram_counter(words):
    return sum(n * (n - 1) / 2 for n in Counter(frozenset(word) for word in words).values())
