from collections import Counter

def anagram_counter(words):
    return sum(n * (n - 1) // 2 for n in Counter(''.join(sorted(w)) for w in words).values())
