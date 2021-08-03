from functools import reduce
from statistics import median


def partition(n, I=1):
    yield (n,)
    for i in range(I, n // 2 + 1):
        for p in partition(n - i, i):
            yield (i,) + p


def part(n):
    prod = set()
    all = partition(n)
    for i in all:
        prod.add(reduce(lambda a, b: a * b, i))
    return("Range: {0} Average: {1:.2f} Median: {2:.2f}".format(max(prod) - min(prod), sum(prod) / len(prod), median(prod)))
