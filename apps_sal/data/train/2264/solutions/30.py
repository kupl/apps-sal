import sys
from heapq import *


def dijkstra(g, start):
    n = len(g)
    INF = 1 << 61
    dist = [INF] * (n)  # startからの最短距離
    num = [0] * n
    dist[start] = 0
    num[start] = 1
    q = [(0, start)]  # (そこまでの距離、点)
    while q:
        dv, v = heappop(q)
        if dist[v] < dv:
            continue
        for to, cost in g[v]:
            if dv + cost < dist[to]:
                dist[to] = dv + cost
                num[to] = num[v]
                heappush(q, (dist[to], to))
            elif dv + cost == dist[to]:
                num[to] += num[v]
                num[to] %= MOD
    return dist, num


# coding: utf-8
# Your code here!
readline = sys.stdin.readline
read = sys.stdin.read

n, m = list(map(int, readline().split()))
s, t = list(map(int, readline().split()))
s -= 1
t -= 1

g = [[] for _ in range(n)]
edges = []
for _ in range(m):
    a, b, c = list(map(int, readline().split()))
    g[a - 1].append((b - 1, c))
    g[b - 1].append((a - 1, c))
    edges.append((a - 1, b - 1, c))

MOD = 10**9 + 7
dist, num = dijkstra(g, s)
dt, nt = dijkstra(g, t)

# print(dist,dt)
# print(num,nt)

ans = num[t]**2
# print(ans,"original")

D = dist[t]
for i in range(n):
    if dist[i] * 2 == D and dist[i] + dt[i] == dist[t]:
        ans -= ((num[i] * nt[i] % MOD)**2) % MOD

# print(ans,"remove-pt")

for a, b, c in edges:
    da = dist[a]
    db = dist[b]
    if da > db:
        a, b = b, a
        da, db = db, da
    if da * 2 < D and db * 2 > D and dist[a] + dt[b] + c == dist[t]:
        ans -= ((num[a] * nt[b] % MOD)**2) % MOD

print((ans % MOD))
