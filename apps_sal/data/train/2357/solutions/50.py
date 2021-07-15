#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n, m = LI()
a = LI()
s = sum(a)
if m + n < s + n:
    print(0)
else:
    ans = 1
    inv = 1
    for i in range(s+n):
        ans *= m + n - i
        ans %= mod
        inv *= i+1
        inv %= mod
    print(ans * pow(inv, mod-2, mod) % mod)
