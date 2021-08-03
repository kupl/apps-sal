import functools


def max_product(lst, n_largest_elements):
    return functools.reduce(lambda x, y: x * y, sorted(lst, reverse=True)[:n_largest_elements])
