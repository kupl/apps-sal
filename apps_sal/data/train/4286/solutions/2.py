def is_prime(n): return n in (2, 3) or n > 3 and n % 2 and n % 3 and all(n % f and n % (f + 2) for f in range(5, int(n ** .5) + 1, 6))
def solve(n): return next(p for gap in __import__('itertools').count(0) for p in (n - gap, n + gap) if is_prime(p))
