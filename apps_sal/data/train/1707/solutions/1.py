from functools import lru_cache


@lru_cache(maxsize=None)
def cl(p, n):
    if n == 0:
        return 0
    q = -1
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_log(p, n - i))
    return q


def cut_log(p, n):
    return cl(tuple(p), n)
