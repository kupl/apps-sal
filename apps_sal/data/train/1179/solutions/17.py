# cook your dish here
from functools import reduce
import operator as op
import math
t = int(input())


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, list(range(n, n - r, -1)), 1)
    denom = reduce(op.mul, list(range(1, r + 1)), 1)
    return numer // denom  # or / in Python 2


for test in range(t):
    n = int(input())
    # If total sum is not even, then we cant divide array in 2 equal sum arrays
    sum_array = (n * (n + 1)) // 2
    if sum_array % 2 != 0:
        print(0)
        continue
    # 1 2 3 4 5 6 7 8 --  9 10 11 12  ---> divide closest to ideal sum
    ideal_sum = sum_array // 2
    partition_sum = 0
    partition_ind = 0
    n_swap = 0
    for i in range(1, n + 1):
        if i + partition_sum > ideal_sum:
            partition_ind = i - 1
            break
        else:
            partition_sum += i
    n_swap = n - partition_ind
    f = math.factorial
    if partition_sum == ideal_sum:
        if partition_ind >= 2:
            n_swap += ncr(partition_ind, 2)
        if n - partition_ind >= 2:
            n_swap += ncr(n - partition_ind, 2)

    print(n_swap)
