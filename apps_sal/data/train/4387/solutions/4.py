from collections import Counter


def sum_no_duplicates(xs):
    return sum(x for x, c in Counter(xs).items() if c == 1)
