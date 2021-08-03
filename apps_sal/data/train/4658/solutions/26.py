from functools import reduce
from heapq import nlargest


def max_product(lst, n_largest_elements):
    return reduce(int.__mul__, nlargest(n_largest_elements, lst))
