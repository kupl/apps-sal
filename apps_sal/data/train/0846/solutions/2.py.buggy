from collections import deque, Counter, OrderedDict
from heapq import heapify, heappop, heappush
from itertools import groupby, accumulate
from collections import defaultdict
import sys
import math
import bisect
sys.setrecursionlimit(10 ** 5)
def I(): return int(sys.stdin.readline())
def neo(): return list(map(int, sys.stdin.readline().split()))
def Neo(): return list(map(int, sys.stdin.readline().split()))


k, a, b = neo()
if k + 1 < a:
    print(k + 1)
    return
k -= a - 1
q = a + k
if b > a:
    t = k // 2
    a += (b - a) * t
    if k - t * 2 > 0:
        a += 1
    print(max(a, q))
    return
print(q)
