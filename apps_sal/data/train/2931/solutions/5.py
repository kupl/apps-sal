from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    if n < 3:
        return 1
    return f(n - 3) + f(n - 1)


def count_cows(n):
    if not isinstance(n, int):
        return None
    return f(n)
