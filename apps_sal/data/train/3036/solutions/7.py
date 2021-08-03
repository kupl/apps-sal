from functools import lru_cache


@lru_cache(maxsize=None)
def rec(i):
    if not i:
        return ""
    return rec(i - 1) + chr(97 + i - 1) + rec(i - 1)


def abacaba(k):
    return rec(26)[k - 1]
