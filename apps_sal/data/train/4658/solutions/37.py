def max_product(lst, n_largest_elements): return __import__('functools').reduce(lambda a, b: a * b, sorted(lst)[-n_largest_elements:])
