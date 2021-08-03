def max_product(lst, n_largest_elements):
    from operator import mul
    from functools import reduce

    return reduce(mul, sorted(lst)[::-1][:n_largest_elements], 1)
