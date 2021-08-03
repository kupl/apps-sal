from functools import reduce


def max_product(lst, n_largest_elements):
    return reduce(int.__mul__, sorted(lst)[-n_largest_elements:])
