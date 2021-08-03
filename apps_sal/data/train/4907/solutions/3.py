from functools import lru_cache


@lru_cache(maxsize=None)
def candles(m, n, l=0):
    if not m and l < n:
        return 0
    m, l = m + l // n, l % n
    return m + candles(0, n, l + m)
