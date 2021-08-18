from bisect import bisect_left as bl, bisect_right as br, insort
import sys
import heapq
#from math import *
from collections import defaultdict as dd, deque
def data(): return sys.stdin.readline().strip()
def mdata(): return map(int, data().split())


# sys.setrecursionlimit(100000)
mod = int(1e9 + 7)


n = int(data())
t = [{} for i in range(n)]
P = list(mdata())
for i in range(n - 1):
    t[P[i] - 1][i + 1] = 0
A = list(mdata())
flag = True
v = [0] * n
v[0] = max(A[0], 0)
ans = v[0]
for i in range(0, n):
    if A[i] == -1:
        l = []
        for j in t[i]:
            if A[j] != -1:
                l.append(A[j])
        m = 0
        if len(l) > 0:
            m = min(l)
            if m < v[i]:
                print(-1)
                return
            ans += m - v[i]
            v[i] = m
    else:
        v[i] = A[i]
    for j in t[i]:
        if A[j] == -1:
            v[j] = v[i]
        elif A[j] < v[i]:
            print(-1)
            return
        else:
            v[j] = A[j]
        ans += v[j] - v[i]
print(ans)
