from collections import defaultdict
from functools import reduce


def find_part_max_prod(n):
    prods = defaultdict(list)
    for p in sum_part(n):
        prods[reduce(int.__mul__, p)].append(p)
    mx = max(prods.keys())
    return sorted(prods[mx], key=len) + [mx]


def sum_part(n, k=2):
    if n < 5:
        yield [n]
    for i in range(k, n // 2 + 1):
        for part in sum_part(n - i, i):
            yield part + [i]
