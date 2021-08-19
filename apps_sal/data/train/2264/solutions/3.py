import heapq
import sys
input = sys.stdin.readline
(N, M) = map(int, input().split())
(S, T) = map(int, input().split())
mod = 10 ** 9 + 7
e = [[] for _ in range(N + 1)]
for _ in range(M):
    (u, v, c) = map(int, input().split())
    e[u].append((v, c))
    e[v].append((u, c))
hpush = heapq.heappush
hpop = heapq.heappop


class dijkstra:

    def __init__(self, n, e):
        self.e = e
        self.n = n

    def path(self, s):
        d = [float('inf')] * (self.n + 1)
        vis = [0] * (self.n + 1)
        d[s] = 0
        h = [s]
        while len(h):
            v = hpop(h)
            v1 = v % 10 ** 6
            v0 = v // 10 ** 6
            if vis[v1]:
                continue
            vis[v1] = 1
            for p in self.e[v1]:
                d[p[0]] = min(d[p[0]], d[v1] + p[1])
                if vis[p[0]]:
                    continue
                hpush(h, d[p[0]] * 10 ** 6 + p[0])
        return d


dij = dijkstra(N, e)
ps = dij.path(S)
pt = dij.path(T)
dps = [0] * (N + 1)
dpt = [0] * (N + 1)
dps[S] = 1
h = []
for x in range(1, N + 1):
    hpush(h, (ps[x], x))
while len(h):
    (_, x) = hpop(h)
    for (y, c) in e[x]:
        if ps[y] > ps[x] and ps[y] - ps[x] == c:
            dps[y] += dps[x]
            dps[y] %= mod
dpt[T] = 1
h = []
for x in range(1, N + 1):
    hpush(h, (pt[x], x))
while len(h):
    (_, x) = hpop(h)
    for (y, c) in e[x]:
        if pt[y] > pt[x] and pt[y] - pt[x] == c:
            dpt[y] += dpt[x]
            dpt[y] %= mod
res = dps[T] * dpt[S] % mod
for x in range(1, N + 1):
    if ps[x] == pt[x]:
        if ps[x] + pt[x] > ps[T]:
            continue
        res -= dps[x] ** 2 * dpt[x] ** 2 % mod
        res %= mod
for x in range(1, N + 1):
    for (y, c) in e[x]:
        if ps[y] - ps[x] == c and ps[y] * 2 > ps[T] and (ps[x] * 2 < ps[T]):
            if ps[x] + pt[y] + c > ps[T]:
                continue
            res -= dps[x] ** 2 * dpt[y] ** 2 % mod
            res %= mod
print(res)
