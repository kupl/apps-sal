from itertools import combinations


def solve(arr):
    return sum((b - a == c - b for (a, b, c) in combinations(arr, 3)))
