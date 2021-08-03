from collections import defaultdict
from math import log2
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def f(n, q):
    def dfs(i, oi=-1, dpt=0):
        depth[i] = dpt
        parent_2k[0][i] = oi
        for ki, c, d in to[i]:
            if ki == oi:
                continue
            dfs(ki, i, dpt + 1)
        return

    def make_parent(level):
        parent_2kk1 = parent_2k[0]
        for k in range(1, level):
            parent_2kk = parent_2k[k]
            for i in range(n):
                parent1 = parent_2kk1[i]
                if parent1 != -1:
                    parent_2kk[i] = parent_2kk1[parent1]
            parent_2kk1 = parent_2kk
        return

    def lca(u, v):
        dist_uv = depth[u] - depth[v]
        if dist_uv < 0:
            u, v = v, u
            dist_uv *= -1

        k = 0
        while dist_uv:
            if dist_uv & 1:
                u = parent_2k[k][u]
            dist_uv >>= 1
            k += 1

        if u == v:
            return u

        for k in range(int(log2(depth[u])) + 1, -1, -1):
            pu = parent_2k[k][u]
            pv = parent_2k[k][v]
            if pu != pv:
                u = pu
                v = pv
        return parent_2k[0][u]

    to = defaultdict(list)
    root = 0
    depth = [0] * n
    level = int(log2(n)) + 1
    parent_2k = [[-1] * n for _ in range(level)]

    for _ in range(n - 1):
        a, b, c, d = list(map(int, input().split()))
        to[a - 1] += [[b - 1, c - 1, d]]
        to[b - 1] += [[a - 1, c - 1, d]]

    dfs(root)
    make_parent(level)

    qs = [[] for _ in range(n)]
    for qi in range(q):
        x, y, u, v = list(map(int, input().split()))
        qs[u - 1].append([qi, x - 1, y, 1])
        qs[v - 1].append([qi, x - 1, y, 1])
        qs[lca(u - 1, v - 1)].append([qi, x - 1, y, -2])

    cnt_c = [0] * n
    sum_c = [0] * n
    ans = [0] * q

    def dfs2(i, oi=-1, sum_d=0):
        for qi, qc, qd, qk in qs[i]:
            ans[qi] += (sum_d - sum_c[qc] + qd * cnt_c[qc]) * qk
        for ki, c, d in to[i]:
            if ki == oi:
                continue
            cnt_c[c] += 1
            sum_c[c] += d
            dfs2(ki, i, sum_d + d)
            cnt_c[c] -= 1
            sum_c[c] -= d
        return

    dfs2(root)
    for x in ans:
        print(x)


n, q = list(map(int, input().split()))
f(n, q)
