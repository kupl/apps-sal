from functools import reduce
from operator import mul


def select_subarray(arr):
    total = sum(arr)
    m = reduce(mul, arr)
    qs = [(abs(m // x / (total - x)) if total - x else float('inf'), i) for (i, x) in enumerate(arr)]
    q = min(qs)
    result = [[i, arr[i]] for (x, i) in qs if x == q[0]]
    return result[0] if len(result) == 1 else result
