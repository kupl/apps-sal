from heapq import heappush as k, heappop as l


def f(s):
    a = [1 << 50] * N
    a[s] = 0
    p = [(0, s)]
    c = [0] * N
    c[s] = 1
    while p:
        d, v = l(p)
        if d > a[v]:
            continue
        for u, w in G[v]:
            if a[u] == d + w:
                c[u] += c[v]
            if a[u] > d + w:
                a[u] = d + w
                k(p, (d + w, u))
                c[u] = c[v]
    return a, c


m = 10**9 + 7
N, M = map(int, input().split())
N += 1
S, T = map(int, input().split())
G = [[]for _ in [0] * N]
for _ in [0] * M:
    U, V, D = map(int, input().split())
    G[U] += [(V, D)]
    G[V] += [(U, D)]
P, X = f(S)
Q, Y = f(T)
s = P[T]
print((X[T]**2 - (1 - s % 2) * sum((X[i] * Y[i])**2for i in range(N)if P[i] == Q[i] == s // 2) - sum((P[i] + d + Q[j] == s) * (P[i] < Q[i]) * (Q[j] < P[j]) * (X[i] * Y[j])**2for i in range(N)for j, d in G[i])) % m)
