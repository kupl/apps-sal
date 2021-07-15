from functools import reduce
max_product = lambda lst, n_largest_elements: reduce(lambda a,b: a*b, sorted(lst)[-n_largest_elements:])
