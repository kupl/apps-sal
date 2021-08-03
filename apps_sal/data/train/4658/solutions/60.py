from heapq import nlargest
from operator import mul
from functools import reduce


def max_product(lst, n):
    return reduce(mul, nlargest(n, lst))
