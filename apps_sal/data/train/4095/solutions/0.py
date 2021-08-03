from collections import Counter


def added_char(s1, s2):
    return next((Counter(s2) - Counter(s1)).elements())
