max_product = lambda lst, n_largest_elements: __import__('functools').reduce(lambda a,b: a*b, sorted(lst)[-n_largest_elements:])
