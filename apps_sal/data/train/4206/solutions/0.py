from functools import lru_cache


@lru_cache(maxsize=None)
def three_details(n):
    if n <= 3:
        return n == 3
    q, r = divmod(n, 2)
    return three_details(q) + three_details(q + r)
