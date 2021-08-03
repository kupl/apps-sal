def max_product(lst, n_largest_elements):
    from functools import reduce
    from operator import mul
    return reduce(mul, sorted(lst)[-n_largest_elements:])
