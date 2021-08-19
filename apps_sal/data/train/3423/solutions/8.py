def solve(a, n):
    return any((sum(c) % n < 1 for r in range(len(a)) for c in __import__('itertools').combinations(a, r + 1)))
