from collections import Counter

def anagrams(word, words):
    counts = Counter(word)
    return [w for w in words if Counter(w) == counts]
