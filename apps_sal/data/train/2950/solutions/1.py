from itertools import combinations

def solve(xs):
    return sum(1 for a, b, c in combinations(xs, 3) if a - b == b - c)
