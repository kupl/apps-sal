from fractions import Fraction
import sys
import math
import io
import os
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter


def data():
    return sys.stdin.readline().strip()


def mdata():
    return list(map(int, data().split()))


def outl(var):
    sys.stdout.write(' '.join(map(str, var)) + '\n')


def out(var):
    sys.stdout.write(str(var) + '\n')


INF = float('inf')
mod = int(1000000000.0) + 7
for t in range(int(data())):
    n = int(data())
    a1 = mdata()
    a2 = mdata()
    d = dd(int)
    g = [[] for i in range(n + 1)]
    for i in range(n):
        d[a1[i]] += 1
        d[a2[i]] += 1
        if a1[i] == a2[i]:
            continue
        g[a1[i]].append((a2[i], i + 1, 0))
        g[a2[i]].append((a1[i], i + 1, 1))
    if max(d.values()) > 2:
        out(-1)
        continue
    vis = [0] * (n + 1)
    vis1 = [0] * (n + 1)
    ans = []
    for i in range(1, n + 1):
        if vis[i] == 0 and g[i]:
            s = [[], []]
            vis[i] = 1
            s[g[i][0][2]].append(g[i][0][1])
            s[1 - g[i][1][2]].append(g[i][1][1])
            vis[g[i][0][0]] = -1
            vis[g[i][1][0]] = 1
            vis1[g[i][0][1]] = 1
            vis1[g[i][1][1]] = 1
            q = []
            q.append(g[i][0][0])
            q.append(g[i][1][0])
            while q:
                a = q.pop()
                if vis[a] == 1:
                    for nei in g[a]:
                        if vis1[nei[1]] == 0:
                            s[1 - nei[2]].append(nei[1])
                            vis[nei[0]] = -1
                            vis1[nei[1]] = 1
                            q.append(nei[0])
                else:
                    for nei in g[a]:
                        if vis1[nei[1]] == 0:
                            s[1 - nei[2]].append(nei[1])
                            vis[nei[0]] = 1
                            vis1[nei[1]] = 1
                            q.append(nei[0])
            if len(s[0]) < len(s[1]):
                ans += s[0]
            else:
                ans += s[1]
    out(len(ans))
    outl(ans)
