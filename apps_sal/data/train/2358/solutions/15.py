from struct import pack, unpack
import math
from heapq import heapify, heappush as hpush, heappop as hpop
xs, ys, xt, yt = map(int, input().split())
N = int(input())
X = [(xs, ys, 0), (xt, yt, 0)]
for _ in range(N):
    x, y, r = map(int, input().split())
    X.append((x, y, r))

N += 2
DD = [[0] * N for _ in range(N)]
for i in range(N):
    xi, yi, ri = X[i]
    for j in range(N):
        xj, yj, rj = X[j]
        DD[i][j] = max(math.sqrt((xi-xj)**2 + (yi-yj)**2) - (ri+rj), 0)

def dijkstra(n, E, i0=0):
    D = [1 << 40] * n
    D[i0] = 0
    Q = set([i for i in range(n)])
    while Q:
        d = 1 << 40
        for q in Q:
            if D[q] < d:
                i = q
                d = D[q]
        Q.remove(i)
        for j, w in enumerate(DD[i]):
            if j == i: continue
            nd = d + w
            if D[j] > nd:
                D[j] = nd
    return D

print(dijkstra(N, X)[1])
