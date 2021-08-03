from functools import lru_cache


@lru_cache(maxsize=None)
def three_details(n):
    if n in (3, 5, 7):
        return 1
    elif n < 6:
        return 0
    q, r = divmod(n, 2)
    if r:
        return three_details(q) + three_details(q + 1)
    else:
        return three_details(q) * 2
