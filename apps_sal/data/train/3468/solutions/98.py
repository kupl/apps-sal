from collections import Counter


def scramble(s1, s2):
    d1, d2 = Counter(s1), Counter(s2)
    for k, v in list(d2.items()):
        if v > d1[k]:
            return False
    return True
