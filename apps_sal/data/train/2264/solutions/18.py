from heapq import heapify, heappush as hpush, heappop as hpop
import sys


def input():
    return sys.stdin.readline().rstrip()


def dijkstra(n, E, i0=0):
    kk = 18
    mm = (1 << kk) - 1
    h = [i0]
    D = [-1] * n
    done = [0] * n
    D[i0] = 0
    while h:
        x = hpop(h)
        (d, i) = (x >> kk, x & mm)
        if done[i]:
            continue
        done[i] = 1
        for (j, w) in E[i]:
            nd = d + w
            if D[j] < 0 or D[j] > nd:
                if done[j] == 0:
                    hpush(h, (nd << kk) + j)
                    D[j] = nd
    return D


def dijkstra2(n, DD, i0=0):
    L = [0] * n
    L[i0] = 1
    AA = [i for i in V]
    AA.sort(key=lambda x: DD[x])
    for a in AA:
        for (b, c) in E[a]:
            if DD[b] + c == DD[a]:
                L[a] += L[b]
                if L[a] >= P:
                    L[a] -= P
    return L


P = 10 ** 9 + 7
(N, M) = list(map(int, input().split()))
(S, T) = [int(a) - 1 for a in input().split()]
E = [[] for _ in range(N)]
for _ in range(M):
    (a, b, c) = list(map(int, input().split()))
    E[a - 1].append((b - 1, c))
    E[b - 1].append((a - 1, c))
D1 = dijkstra(N, E, S)
D2 = dijkstra(N, E, T)
mad = D1[T]
V = set([i for i in range(N) if D1[i] + D2[i] == mad])
X = dijkstra2(N, D1, S)
Y = dijkstra2(N, D2, T)
ans = X[T] ** 2 % P
for i in V:
    if D1[i] == D2[i]:
        ans = (ans - (X[i] * Y[i] % P) ** 2) % P
for a in V:
    for (b, c) in E[a]:
        if D1[a] + c == D1[b]:
            if D1[a] * 2 < mad < D1[b] * 2:
                ans = (ans - (X[a] * Y[b] % P) ** 2) % P
print(ans)
