from collections import Counter


def anagram_counter(words):
    anag = Counter((tuple(sorted(Counter(w).items())) for w in words))
    return sum((n * (n - 1) // 2 for n in anag.values()))
