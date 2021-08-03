from collections import Counter


def scramble(s1, s2):
    se1 = Counter(s1)
    se2 = Counter(s2)
    return se1 | se2 == se1
