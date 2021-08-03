from functools import reduce
from operator import mul


def find_min_max_product(arr, k):
    if k > len(arr):
        return None

    if k == 1:
        return min(arr), max(arr)

    if k == len(arr):
        prod = reduce(mul, arr)
        return prod, prod

    arr = sorted(arr)
    prods = []
    for i in range(k + 1):
        nums = arr[:k - i] + (arr[-i:] if i else [])
        prods.append(reduce(mul, nums))

    return min(prods), max(prods)
