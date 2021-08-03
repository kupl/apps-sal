from itertools import accumulate
from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush, heappop, heapify
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline


M = mod = 998244353
def factors(n): return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n): return pow(n, mod - 2, mod)


def li(): return [int(i) for i in input().rstrip('\n').split()]
def st(): return input().rstrip('\n')
def val(): return int(input().rstrip('\n'))
def li2(): return [i for i in input().rstrip('\n')]
def li3(): return [int(i) for i in input().rstrip('\n')]


for _ in range(val()):
    n = val()
    l = li3()

    d = defaultdict(list)
    ans = {}
    curr = 1
    for i in range(n):
        if len(d[1 - l[i]]):
            d[l[i]].append(d[1 - l[i]].pop())
            ans[i] = d[l[i]][-1]
        else:
            d[l[i]].append(curr)
            ans[i] = curr
            curr += 1
    print(curr - 1)
    for i in range(n):
        print(ans[i], end=' ')
    print()
