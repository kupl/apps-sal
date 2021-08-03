from itertools import groupby


def count_adjacent_pairs(s):
    return sum(next(y) == next(y, 0) for x, y in groupby(s.lower().split()))
