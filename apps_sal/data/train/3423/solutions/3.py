from itertools import combinations

def solve(x, n):
    return any(sum(cb) % n == 0 for k in range(len(x)) for cb in combinations(x, k + 1))
