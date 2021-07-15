from collections import Counter

def anagram_counter(a):
    return sum(n * (n - 1) / 2 for n in Counter("".join(sorted(x)) for x in a).values())
