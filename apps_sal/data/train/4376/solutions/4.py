from functools import lru_cache


@lru_cache(maxsize=None)
def count_pal(n):
    if n == 0:
        return [0, 0]
    current = 9 * 10 ** (n - 1 >> 1)
    previous = count_pal(n - 1)[1]
    return [current, current + previous]
