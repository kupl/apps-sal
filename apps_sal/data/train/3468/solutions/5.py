from collections import Counter

def scramble(s1,s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    return not (c2 -c1).values()
