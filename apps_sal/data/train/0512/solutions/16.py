
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, q = map(int, input().split())
edges = [[] for i in range(n)]
for i in range(n - 1):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    edges[a].append((b, c, d))
    edges[b].append((a, c, d))

dep = [0] * n
par = [[-1] * n for i in range(18)]
dis = [0] * n


def dfs(p, v, d, dd):
    dep[v] = d
    par[0][v] = p
    dis[v] = dd
    for w, _, dist in edges[v]:
        if w != p:
            dfs(v, w, d + 1, dd + dist)


def lca(a, b):
    if dep[a] > dep[b]:
        a, b = b, a
    for i in range(18):
        if (dep[b] - dep[a]) & 1 << i:
            b = par[i][b]
    if a == b:
        return a
    for i in range(18)[::-1]:
        if par[i][a] != par[i][b]:
            a = par[i][a]
            b = par[i][b]
    return par[0][a]


dfs(-1, 0, 0, 0)

for i in range(17):
    for j in range(n):
        par[i + 1][j] = par[i][par[i][j]]


ans = [0] * q
v_need = [[] for i in range(n)]
for i in range(q):
    x, y, u, v = map(int, input().split())
    x -= 1
    u -= 1
    v -= 1
    l = lca(u, v)
    v_need[u].append((i, x, y, 1))
    v_need[v].append((i, x, y, 1))
    v_need[l].append((i, x, y, -2))

color = [0] * n
cdist = [0] * n


def dfs2(cur, par):
    for i, x, y, k in v_need[cur]:
        ans[i] += k * (dis[cur] - cdist[x] + y * color[x])
    for to, x, y, in edges[cur]:
        if to == par:
            continue
        color[x] += 1
        cdist[x] += y
        dfs2(to, cur)
        color[x] -= 1
        cdist[x] -= y


dfs2(0, -1)

for i in ans:
    print(i)
