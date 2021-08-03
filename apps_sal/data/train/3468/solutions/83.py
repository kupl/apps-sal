from collections import Counter


def scramble(s1, s2):
    t1 = Counter(s1)
    t2 = Counter(s2)
    d = t2 - t1
    return len(d) == 0
