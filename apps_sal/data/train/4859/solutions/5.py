from math import factorial as fact
from collections import Counter
from functools import reduce


def ssc_forperm(arr):
    cnt = Counter(arr)
    nPerms = fact(len(arr)) // reduce(int.__mul__, map(fact, cnt.values()), 1)
    sIdx = -~len(arr) * len(arr) >> 1
    arr = sorted(arr)
    return [{'total perm': nPerms}, {'total ssc': sum((v * sIdx * nPerms // len(arr) for v in arr))}, {'max ssc': sum((v * i for (i, v) in enumerate(arr, 1)))}, {'min ssc': sum((v * i for (i, v) in enumerate(reversed(arr), 1)))}]
