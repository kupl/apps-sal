from itertools import groupby


def count_repeats(s):
    return len(s) - len(list(groupby(s)))
