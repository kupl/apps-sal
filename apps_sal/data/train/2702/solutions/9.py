from collections import Counter

def create_anagram(s, t):
    cs, ct = Counter(s), Counter(t)
    return sum(n for _, n in (ct - cs).items())
