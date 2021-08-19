from heapq import nlargest
from functools import reduce
from operator import mul


def max_product(lst, k):
    return reduce(mul, nlargest(k, lst))
