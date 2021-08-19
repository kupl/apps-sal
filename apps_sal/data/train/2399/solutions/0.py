from sys import stdin, stdout
import functools
import sys
import os
import math
T = int(input())
for _ in range(T):
    (N, M) = list(map(int, input().split()))
    DS = [0] * (N + 1)
    ES = []
    g = [[] for _ in range(N + 1)]
    for _ in range(M):
        (t, u, v) = list(map(int, input().split()))
        ES.append([t, u, v])
        if t == 1:
            DS[u] += 1
        g[u].append(len(ES) - 1)
        g[v].append(len(ES) - 1)
    q = []
    for u in range(1, N + 1):
        if DS[u] == 0:
            q.append(u)
    while len(q) > 0:
        u = q.pop()
        if DS[u] > 0:
            continue
        for e in g[u]:
            (t, u0, v0) = ES[e]
            if t == 1:
                if v0 == u:
                    DS[u0] -= 1
                    if DS[u0] == 0:
                        q.append(u0)
            elif t == 0:
                v = v0 if u0 == u else u0
                ES[e] = [1, v, u]
    md = max(DS)
    if md > 0:
        print('NO')
    else:
        print('YES')
        for e in ES:
            print(e[1], e[2])
