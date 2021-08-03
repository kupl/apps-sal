from functools import lru_cache


@lru_cache(maxsize=None)
def count_subsequences(a, b):
    if not a:
        return 1
    if not b:
        return 0
    i = b.find(a[0])
    if i == -1:
        return 0
    return count_subsequences(a, b[i + 1:]) + count_subsequences(a[1:], b[i + 1:])
