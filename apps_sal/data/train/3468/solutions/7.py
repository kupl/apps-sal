from collections import Counter


def scramble(s1, s2):
    return not (Counter(s2) - Counter(s1))
