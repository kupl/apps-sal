import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, Q = MAP()

event = [None]*(2*N+Q)
Xl = [0]*N
for i in range(N):
    S, T, X = MAP()
    event[2*i] = (S-X, 1, X)
    event[2*i+1] = (T-X, 0, X)
    Xl[i] = X

t = 2*N
for i in range(Q):
    D = INT()
    event[t+i] = (D, 2, 0)


event.sort()
p = []
q = []
for t, c, x in event:
    if c == 0:
        heappush(q, x)
    elif c == 1:
        heappush(p, x)
    else:
        while q and p[0] == q[0]:
            heappop(p)
            heappop(q)
        print((-1 if not p else p[0]))

