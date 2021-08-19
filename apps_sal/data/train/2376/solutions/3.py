from sys import stdin, stdout
import functools
import sys
import os
import math

# sys.setrecursionlimit(10**6)

T = int(input())

for _ in range(T):
    N, K = list(map(int, input().split()))
    DS = [0] * (N + 1)
    LeafNum = [0] * (N + 1)
    g = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = list(map(int, input().split()))
        DS[u] += 1
        DS[v] += 1
        g[u].append(v)
        g[v].append(u)

    for u in range(1, N + 1):
        if DS[u] == 1:
            for v in g[u]:
                LeafNum[v] += 1

    if K == 1:
        print(N - 1)
        continue

    q = set()
    for u in range(1, N + 1):
        if LeafNum[u] >= K:
            q.add(u)

    ans = 0
    while len(q) > 0:
        u = q.pop()
        nl = LeafNum[u]
        ans += int(nl / K)
        LeafNum[u] = nl % K
        dn = int(nl / K) * K
        DS[u] -= int(nl / K) * K
        if DS[u] == 1:
            for v in g[u]:
                if DS[v] == 1 and dn > 0:
                    dn -= 1
                    continue

                LeafNum[v] += 1
                if LeafNum[v] >= K and v not in q:
                    q.add(v)
    print(ans)
