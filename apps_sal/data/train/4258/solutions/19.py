from fractions import Fraction
from functools import lru_cache

@lru_cache(maxsize=None)
def rec(n):
    if not n: return 0
    return Fraction(1, 3*n-2) + rec(n-1)

# This is overkill for this kata
def series_sum(n):
    return f"{float(rec(n)):.2f}"
