from itertools import combinations

def solve(a):
    return sum(q + (q - p) in a for p, q in combinations(a, 2))
