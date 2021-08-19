from collections import Counter


def scramble(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    c1.subtract(c2)
    c3 = [v < 0 for (k, v) in c1.items() if k in c2.keys()]
    return not any(c3)
