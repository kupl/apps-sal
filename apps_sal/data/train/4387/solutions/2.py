from collections import Counter


def sum_no_duplicates(l):
    return sum((k for (k, v) in list(Counter(l).items()) if v == 1))
