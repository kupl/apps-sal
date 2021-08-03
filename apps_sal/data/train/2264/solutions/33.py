import heapq as h


def f(s):
    a = [1 << 50] * N
    a[s] = 0
    p = [(0, s)]
    c = [0] * N
    c[s] = 1
    while p:
        d, v = h.heappop(p)
        if d <= a[v]:
            for u, w in G[v]:
                if a[u] > d + w:
                    a[u] = d + w
                    h.heappush(p, (d + w, u))
                    c[u] = 0
                if a[u] == d + w:
                    c[u] += c[v]
    return a, c


def n(): return map(int, input().split())


N, M = n()
N += 1
S, T = n()
G = [[]for _ in [0] * N]
for _ in [0] * M:
    U, V, D = n()
    G[U] += [(V, D)]
    G[V] += [(U, D)]
P, X = f(S)
Q, Y = f(T)
s = P[T]
print((X[T]**2 - (1 - s % 2) * sum((X[i] * Y[i])**2for i in range(N)if P[i] == Q[i] == s // 2) - sum((P[i] + d + Q[j] == s) * (P[i] < Q[i]) * (Q[j] < P[j]) * (X[i] * Y[j])**2for i in range(N)for j, d in G[i])) % (10**9 + 7))
