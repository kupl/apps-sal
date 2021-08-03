from itertools import groupby


def count_adjacent_pairs(stg):
    return sum(1 for _, g in groupby(stg.lower().split()) if len(list(g)) > 1)
