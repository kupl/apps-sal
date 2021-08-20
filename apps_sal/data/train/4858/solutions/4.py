from functools import lru_cache


@lru_cache(maxsize=None)
def j(n):
    return n - a(j(n - 1)) if n else 0


@lru_cache(maxsize=None)
def a(n):
    return n - j(a(n - 1)) if n else 1


def john(n):
    return [j(i) for i in range(n)]


def ann(n):
    return [a(i) for i in range(n)]


def sum_john(n):
    return sum(john(n))


def sum_ann(n):
    return sum(ann(n))
