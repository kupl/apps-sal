from collections import Counter

def scramble(s1, s2):
    s1 = Counter(s1)
    s2 = Counter(s2)
    return len([c for c in s2 if s1[c] >= s2[c]]) == len(s2.keys())
