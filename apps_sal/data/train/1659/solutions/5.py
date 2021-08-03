import functools


@functools.lru_cache(1 << 16)
def f(n, m):
    if n == 0:
        return 1
    return sum(f(n - i, i) for i in range(1, min(n, m) + 1))


def exp_sum(n):
    return f(n, n)
