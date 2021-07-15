def max_product(lst, n_largest_elements):
    from functools import reduce
    return reduce(lambda x, y: x * y, sorted(lst)[-n_largest_elements:])
