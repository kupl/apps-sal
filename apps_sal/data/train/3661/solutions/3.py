from collections import defaultdict
from operator import mul
from functools import reduce


def partitions(n, s=float('inf')):
    if not n:
        yield []
        return
    for i in range(min(n, s), 0, -1):
        for p in partitions(n - i, i):
            yield [i] + p


def find_part_max_prod(n):
    products = defaultdict(list)
    for p in partitions(n):
        products[reduce(mul, p)].append(p)
    m = max(products)
    return products[m] + [m]
