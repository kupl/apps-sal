n = int(input())
edges = [[int(x) for x in input().split()] for i in range(n - 1)]
edges = sorted(edges)
use_count = [0] + [int(input()) for i in range(n)]
(lo, hi) = (0, 10000)


def getpar(par, u):
    if par[par[u]] == par[u]:
        return par[u]
    par[u] = getpar(par, par[u])
    return par[u]


def unite(par, sz, use, u, v):
    u = getpar(par, u)
    v = getpar(par, v)
    par[u] = v
    sz[v] += sz[u]
    use[v] += use[u]


def solve(fp):
    par = [i for i in range(n + 1)]
    sz = [1 for i in range(n + 1)]
    use = [use_count[i] for i in range(n + 1)]
    for edge in edges:
        if edge[2] < fp:
            unite(par, sz, use, edge[0], edge[1])
    total_use = sum(use_count)
    for i in range(n + 1):
        p = getpar(par, i)
        if p == i:
            if total_use - use[p] < sz[p]:
                return False
    return True


while lo < hi:
    mid = (lo + hi + 1) // 2
    if solve(mid):
        lo = mid
    else:
        hi = mid - 1
print(lo)
