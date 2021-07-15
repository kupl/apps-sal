import operator
import functools
def max_product(lst, n_largest_elements):
    return functools.reduce(operator.mul,sorted(lst,reverse=True)[:n_largest_elements])
