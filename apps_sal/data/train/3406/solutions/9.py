from functools import lru_cache


@lru_cache()
def f(n):
    return 1 if n <= 0 else n - m(f(n - 1))


@lru_cache()
def m(n):
    return 0 if n <= 0 else n - f(m(n - 1))
