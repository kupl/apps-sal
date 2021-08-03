from functools import lru_cache
from math import factorial as f
@lru_cache(maxsize=None)
def all_permuted(n): return [1, 0][n] if n < 2 else (n - 1) * (all_permuted(n - 1) + all_permuted(n - 2))


def fixed_points_perms(n, k): return all_permuted(n - k) * f(n) // (f(k) * f(n - k)) if n >= k else 0
