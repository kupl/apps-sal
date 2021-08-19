import sys
import heapq
import functools
import collections
import math
import random
from collections import Counter, defaultdict


def solve(srr, k):
    console('----- solving ------')
    console(srr, k)
    ones = 0
    zeroes = 0
    for i in range(k):
        sett = set(srr[i::k])
        if '1' in sett and '0' in sett:
            return 'NO'
        if '1' in sett:
            ones += 1
        if '0' in sett:
            zeroes += 1
    if ones > k // 2 or zeroes > k // 2:
        return 'NO'
    return 'YES'


def console(*args):
    print('\x1b[36m', *args, '\x1b[0m', file=sys.stderr)
    return


for case_num in range(int(input())):
    (_, k) = list(map(int, input().split()))
    srr = input()
    res = solve(srr, k)
    print(res)
