from collections import Counter


def scramble(s1, s2):
    l = Counter(s1)
    w = Counter(s2)
    diff = w - l
    return len(diff) == 0
