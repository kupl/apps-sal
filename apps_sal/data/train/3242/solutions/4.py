from functools import reduce
from operator import mul


def maximum_product(arr):
    prods = {}

    for e in sorted(set(arr))[::-1]:
        a = arr[:]
        a.remove(e)
        prods[reduce(mul, a)] = e

    return prods[max(prods)]
