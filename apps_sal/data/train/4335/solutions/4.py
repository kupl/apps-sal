from collections import Counter


def anagrams(word, words):
    (n, c) = (len(word), Counter(word))
    return [w for w in words if len(w) == n and Counter(w) == c]
