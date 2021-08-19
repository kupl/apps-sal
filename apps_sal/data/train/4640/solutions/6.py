from itertools import combinations


def int_diff(arr, n):
    return sum((abs(c1 - c2) == n for (c1, c2) in combinations(arr, 2)))
