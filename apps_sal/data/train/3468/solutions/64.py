from collections import Counter


def scramble(s1, s2):
    return True if sum((Counter(s2) & Counter(s1)).values()) == len(s2) else False
