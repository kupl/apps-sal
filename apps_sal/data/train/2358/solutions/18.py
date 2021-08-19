#from collections import deque,defaultdict
from heapq import heappush, heappop
from math import sqrt
def printn(x): return print(x, end='')
def inn(): return int(input())


def inl(): return list(map(int, input().split()))
def inm(): return map(int, input().split())
def ins(): return input().strip()


DBG = True  # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353


def ddprint(x):
    if DBG:
        print(x)


#import math,heapq

def pdist(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


xs, ys, xt, yt = inm()
n = inn()
cir = []
for i in range(n):
    x, y, r = inm()
    cir.append((x, y, r))
dst = [[0] * (n + 2) for i in range(n + 2)]
dst[n][n + 1] = dst[n + 1][n] = pdist(xs, ys, xt, yt)
for i in range(n):
    x, y, r = cir[i]
    dst[n][i] = dst[i][n] = max(0.0, pdist(xs, ys, x, y) - r)
    dst[n + 1][i] = dst[i][n + 1] = max(0.0, pdist(xt, yt, x, y) - r)
    for j in range(i + 1, n):
        xx, yy, rr = cir[j]
        dst[j][i] = dst[i][j] = \
            max(0.0, pdist(xx, yy, x, y) - rr - r)

if False and DBG:
    for i in range(n + 2):
        ddprint(dst[i])

cost = [float(BIG)] * (n + 2)
q = [(0.0, n)]
while len(q) > 0:
    d, p = heappop(q)
    #ddprint(f"{d=} {p=}")
    if cost[p] <= d:
        continue
    cost[p] = d
    for v in range(n + 2):
        newdist = d + dst[p][v]
        if v != p and newdist < cost[v]:
            heappush(q, (newdist, v))

print(cost[n + 1])
