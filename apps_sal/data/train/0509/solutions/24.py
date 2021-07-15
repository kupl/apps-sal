import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

def inp():
    return int(input())
def inps():
    return input().rstrip()
def inpl():
    return list(map(int, input().split()))
def inpls():
    return list(map(str, input().split()))
def _debug(obj):
    print(obj, file=sys.stderr)

# import decimal
# from decimal import Decimal
# decimal.getcontext().prec = 10

# from heapq import heappush, heappop, heapify
# import math
from math import gcd, floor, ceil, factorial
import itertools as it
from collections import deque, defaultdict
from collections import Counter

def lcd(a, b):
    return a * b // gcd(a, b)

def chmin(dp, i, x):
    if x < dp[i]: dp[i] = x; return True
    return False

def chmax(dp, i, x): 
    if x > dp[i]: dp[i] = x; return True
    return False

# ---------------------------------------

N, M = inpl()
graph = [[] for i in range(N)]
for i in range(M):
    u, v, c = inpl()
    graph[u-1].append([v-1, c])
    graph[v-1].append([u-1, c])
ans = [0] * N
ans[0] = 1
q = deque()
q.append(0)
while True:
    if not q:
        break
    i = q.popleft()
    for g in graph[i]:
        j = g[0]
        c = g[1]
        if ans[j] != 0:
            continue
        if ans[i] == c:
            if c + 1 <= N:
                ans[j] = c + 1
            else:
                ans[j] = c - 1
        else:
            ans[j] = c
        q.append(j)
for i in ans:
    print(i)
