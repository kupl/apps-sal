from itertools import combinations


def count_inversion(lst):
    return sum(a > b for a, b in combinations(lst, 2))
