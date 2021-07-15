from functools import lru_cache

@lru_cache(maxsize=None)
def padovan(n):
    return n<3 or padovan(n-2) + padovan(n-3)
