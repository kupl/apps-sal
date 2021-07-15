from functools import reduce 
from operator import mul

def max_product(lst, n_largest_elements):
    lst = sorted(lst, reverse=True)[:n_largest_elements]
    return reduce(mul, lst)

