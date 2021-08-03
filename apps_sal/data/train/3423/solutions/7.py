from itertools import combinations


def solve(arr, n):
    return next((True for x in range(1, len(arr) + 1) for c in combinations(arr, x) if not sum(c) % n), False)
