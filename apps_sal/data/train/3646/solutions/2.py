from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    return (n - 1) * (f(n - 1) + f(n - 2)) if n > 2 else int(n != 1)


def fixed_points_perms(n, k):
    return n * fixed_points_perms(n - 1, k - 1) // k if k else f(n)
