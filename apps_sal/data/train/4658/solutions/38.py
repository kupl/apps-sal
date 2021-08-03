from functools import reduce
def max_product(lst, n_largest_elements): return reduce(lambda a, b: a * b, sorted(lst)[-n_largest_elements:])
