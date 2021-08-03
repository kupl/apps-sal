# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2019/11/30 18:18

"""

T = int(input())
for ti in range(T):
    N, M, K = list(map(int, input().split()))

    G = collections.defaultdict(list)
    for i in range(M):
        u, v = list(map(int, input().split()))
        G[u].append(v)
        G[v].append(u)

    museums = [0] + [int(x) for x in input().split()]

    vis = [False] * (N + 1)
    counts = []
    for s in range(1, N + 1):
        if vis[s]:
            continue
        vis[s] = True
        count = 0
        q = [s]
        while q:
            u = q.pop()
            count += museums[u]
            for v in G[u]:
                if not vis[v]:
                    vis[v] = True
                    q.append(v)
        counts.append(count)

    if len(counts) < K:
        print(-1)
    else:
        counts.sort(reverse=True)
        if K == 1:
            print(counts[0])
        elif K % 2 == 0:
            print(sum(counts[:K // 2]) + sum(counts[-(K // 2):]))
        else:
            print(sum(counts[:K // 2 + 1]) + sum(counts[-(K // 2):]))
