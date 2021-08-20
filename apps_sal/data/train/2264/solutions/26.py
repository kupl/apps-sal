from heapq import heappush, heappop


def f(s):
    a = [1 << 50] * N
    a[s] = 0
    p = [(0, s)]
    while p:
        (d, v) = heappop(p)
        if d > a[v]:
            continue
        for (u, w) in G[v]:
            if a[u] > d + w:
                a[u] = d + w
                heappush(p, (d + w, u))
    return a


def g(a, s):
    w = [0] * N
    w[s] = 1
    b = [0] * N
    b[s] = 1
    p = [(0, s)]
    while p:
        (d, v) = heappop(p)
        for (u, d) in G[v]:
            if a[v] + d == a[u]:
                w[u] = (w[u] + w[v]) % m
                if not b[u]:
                    heappush(p, (a[u], u))
                    b[u] = 1
    return w


m = 10 ** 9 + 7
(N, M) = map(int, input().split())
(S, T) = map(int, input().split())
S -= 1
T -= 1
G = [[] for _ in [0] * N]
for _ in [0] * M:
    (U, V, D) = map(int, input().split())
    U -= 1
    V -= 1
    G[U] += [(V, D)]
    G[V] += [(U, D)]
dS = f(S)
dT = f(T)
wS = g(dS, S)
wT = g(dT, T)
s = dS[T]
a = (wS[T] ** 2 - (1 - s % 2) * sum(((wS[i] * wT[i]) ** 2 for i in range(N) if dS[i] == dT[i] == s // 2))) % m
for i in range(N):
    for (j, d) in G[i]:
        if dS[i] + d + dT[j] == s:
            if (dS[i] < dT[i]) * (dT[j] < dS[j]):
                a = (a - (wS[i] * wT[j]) ** 2) % m
print(a)
