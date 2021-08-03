from functools import lru_cache


@lru_cache()
def padovan(n):
    return 1 if n < 3 else padovan(n - 2) + padovan(n - 3)
