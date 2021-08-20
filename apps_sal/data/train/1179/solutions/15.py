from functools import reduce
import operator as op
import math
t = int(input())


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, list(range(n, n - r, -1)), 1)
    denom = reduce(op.mul, list(range(1, r + 1)), 1)
    return numer // denom


for test in range(t):
    n = int(input())
    sum_array = n * (n + 1) // 2
    if sum_array % 2 != 0:
        print(0)
        continue
    n_swap = 0
    d = 1 + 4 * sum_array
    partition_ind = (math.sqrt(d) - 1) / 2
    n_swap = n - math.floor(partition_ind)
    f = math.factorial
    if partition_ind.is_integer():
        partition_ind = int(partition_ind)
        if partition_ind >= 2:
            n_swap += ncr(partition_ind, 2)
        if n - partition_ind >= 2:
            n_swap += ncr(n - partition_ind, 2)
    print(n_swap)
