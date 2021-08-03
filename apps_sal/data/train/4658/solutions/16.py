import functools as f


def max_product(lst, n):
    return f.reduce(lambda a, b: a * b, sorted(lst)[-n:])
