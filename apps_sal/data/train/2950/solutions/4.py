from itertools import combinations


def solve(arr):
    S = set(arr)
    return sum(2 * y - x in S for x, y in combinations(arr, 2))
