from collections import *
import sys
sys.setrecursionlimit(10 ** 9)


def solve():

    def dfs(u, f):
        G[u].append(f)
        G1[f].append(u)
        for v in g[u]:
            if v not in used:
                used.add(v)
                dfs(v, f)
    (n, m) = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    edges.sort(key=lambda item: item[2])
    G = defaultdict(list)
    G1 = defaultdict(list)
    en = 0
    cnt = 0
    while en < len(edges):
        st = en
        g = defaultdict(list)
        used = set()
        while en < len(edges) and edges[en][2] == edges[st][2]:
            (x, y) = (edges[en][0], edges[en][1])
            g[x].append(y)
            g[y].append(x)
            en += 1
        for k in g:
            if k not in used:
                used.add(k)
                dfs(k, cnt)
                cnt += 1
    usedG = set()
    usedP = set()
    deq = deque()
    deq.append(1)
    usedP.add(1)
    step = 0
    while deq:
        siz = len(deq)
        for _ in range(siz):
            f = deq.popleft()
            if f == n:
                print(step)
                return
            for g in G[f]:
                if g not in usedG:
                    usedG.add(g)
                    for p in G1[g]:
                        if p not in usedP:
                            usedP.add(p)
                            deq.append(p)
        step += 1
    print(-1)


solve()
