from itertools import combinations


def solve(xs):
    return sum(a - b == b - c for a, b, c in combinations(xs, 3))
