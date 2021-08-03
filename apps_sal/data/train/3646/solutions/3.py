from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    if n <= 2:
        return n - 1
    return (n - 1) * (f(n - 1) + f(n - 2))


def fixed_points_perms(n, k):
    if n == k:
        return 1
    elif k >= n - 1:
        return 0
    elif k == 0:
        return f(n)
    return n * fixed_points_perms(n - 1, k - 1) // k
