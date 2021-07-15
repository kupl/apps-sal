from operator import mul
from functools import reduce
def max_product(lst, n_largest_elements):
    return reduce(mul, sorted(lst)[::-1][:n_largest_elements])
