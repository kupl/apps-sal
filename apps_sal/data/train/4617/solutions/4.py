from itertools import accumulate, repeat, chain, islice
from operator import mul

gen, memo = accumulate(chain((1,), repeat(2)), mul), []


def powers_of_two(n):
    if len(memo) <= n:
        memo.extend(islice(gen, n - len(memo) + 1))
    return memo[:n + 1]
