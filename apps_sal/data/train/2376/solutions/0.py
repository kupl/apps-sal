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
    n, k = li()
    d = defaultdict(set)
    for i in range(n - 1):
        a, b = li()
        d[a].add(b)
        d[b].add(a)
    thistime = 1
    he = deque()
    visited = {}
    for i in d:
        if len(d[i]) == 1:
            visited[i] = 1
            he.append(i)
    ans = 0
    counts = defaultdict(int)

    while he:
        i = he.popleft()
        for j in list(d[i]):
            counts[j] += 1
            d[i].remove(j)
            d[j].remove(i)
            if counts[j] == k:
                thistime = 1
                ans += 1
                counts[j] = 0
                if len(d[j]) == 1:
                    if j not in visited:
                        he.append(j)
                    visited[j] = 1
    print(ans)
