from operator import mul
from functools import reduce
from collections import deque
from itertools import compress
from heapq import nsmallest, nlargest


def find_min_max_product(arr, k):
    if k <= len(arr):
        large = nlargest(k, arr)[::-1]
        small = nsmallest(min(k, len(arr) - k), arr)
        darr = small + large
        mask = deque([0] * len(small) + [1] * len(large))
        res = []
        for b in range(len(darr)):
            res.append(reduce(mul, compress(darr, mask)))
            mask.rotate(-1)
        return min(res), max(res)
