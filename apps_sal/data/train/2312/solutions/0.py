from functools import lru_cache
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


n, q = li()


queue = [-1] * 20

ans = [[-1] * 20 for i in range(n + 1)]
l = li()
for i, curr in enumerate(l):

    for j in range(20):
        if curr >> j & 1:
            for k in range(20):
                ans[i][k] = max(ans[i][k], ans[queue[j]][k])
            ans[i][j] = i

    for j in range(20):
        queue[j] = max(queue[j], ans[i][j])


queries = []
for i in range(q):
    queries.append(li())
for i in range(q):
    a, b = queries[i]
    a -= 1
    b -= 1

    currans = 0

    for j in range(20):
        if (l[a] >> j) & 1 and ans[b][j] >= a:
            currans = 1
            break
    print('Shi' if currans else 'Fou')
