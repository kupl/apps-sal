from itertools import permutations
from bisect import bisect_left
memo = [int(''.join(x)) for x in permutations('0123456789') if x[0] != '0']


def get_sequence(offset, size):
    i = bisect_left(memo, offset)
    return memo[i:i + size]
