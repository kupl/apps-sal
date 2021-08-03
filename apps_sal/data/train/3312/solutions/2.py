from collections import Counter


def anagram_counter(words):
    return sum(n * (n - 1) >> 1 for n in Counter(''.join(sorted(word)) for word in words).values())
