from itertools import groupby


def count_repeats(txt):
    return len(txt) - sum(1 for _ in groupby(txt))
