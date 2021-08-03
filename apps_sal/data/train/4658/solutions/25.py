import heapq
from functools import reduce


def max_product(lst, n):
    return reduce(lambda x, y: x * y, heapq.nlargest(n, lst))
