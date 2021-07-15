from functools import lru_cache
@lru_cache(maxsize=None)
def all_permuted(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    return (n-1)*(all_permuted(n-1)+all_permuted(n-2))
