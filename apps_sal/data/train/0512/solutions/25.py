import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 5 + 5)


def solve(n, links, queries):
    def _query(a, b, data, m0, INF):
        yield INF
        a += m0
        b += m0
        while a < b:
            if b & 1:
                b -= 1
                yield data[b - 1]
            if a & 1:
                yield data[a - 1]
                a += 1
            a >>= 1
            b >>= 1

    def query(u, v):
        fu = first_appear[u]
        fv = first_appear[v]
        if fu > fv:
            fu, fv = fv, fu
        return euler_tour[min(_query(fu, fv + 1, data, m0, INF))[1]]

    def dfs(v, p, dep):
        first_appear[v] = len(euler_tour)
        depth[v] = dep
        euler_tour.append(v)
        for u, _, _ in links[v]:
            if u == p:
                continue
            dfs(u, v, dep + 1)
            euler_tour.append(v)

    def dfs2(v, p, tmp_dists, total_dist):
        for x, arr in list(v_queries[v].items()):
            arr[0] = total_dist - tmp_dists[x][0]
            arr[1] = tmp_dists[x][1]
        for u, uc, ud in links[v]:
            if u == p:
                continue
            tmp_dists[uc][0] += ud
            tmp_dists[uc][1] += 1
            dfs2(u, v, tmp_dists, total_dist + ud)
            tmp_dists[uc][0] -= ud
            tmp_dists[uc][1] -= 1

    INF = (n, None)

    euler_tour = []
    first_appear = [0] * n
    depth = [0] * n

    dfs(0, -1, 0)

    m = 2 * n
    m0 = 2 ** (m - 1).bit_length()
    data = [INF] * (2 * m0)
    for i, v in enumerate(euler_tour):
        data[m0 - 1 + i] = (depth[v], i)
    for i in range(m0 - 2, -1, -1):
        data[i] = min(data[2 * i + 1], data[2 * i + 2])

    v_queries = [{} for _ in range(n)]
    lca = []
    for i, (x, y, u, v) in enumerate(queries):
        w = query(u, v)
        lca.append(w)
        v_queries[u][x] = [0, 0]
        v_queries[v][x] = [0, 0]
        if w != 0:
            v_queries[w][x] = [0, 0]

    tmp_dists = defaultdict(lambda: [0, 0])
    dfs2(0, -1, tmp_dists, 0)

    ans = []
    for w, (x, y, u, v) in zip(lca, queries):
        qu = v_queries[u][x]
        qv = v_queries[v][x]
        du = qu[0] + qu[1] * y
        dv = qv[0] + qv[1] * y
        if w == 0:
            ans.append(du + dv)
            continue
        qw = v_queries[w][x]
        dw = qw[0] + qw[1] * y
        ans.append(du + dv - 2 * dw)

    return ans


n, q = list(map(int, input().split()))
links = [set() for _ in range(n)]
lines = sys.stdin.readlines()
for line in lines[:n - 1]:
    a, b, c, d = list(map(int, line.split()))
    a -= 1
    b -= 1
    links[a].add((b, c, d))
    links[b].add((a, c, d))
queries = []
for line in lines[n - 1:]:
    x, y, u, v = list(map(int, line.split()))
    u -= 1
    v -= 1
    queries.append((x, y, u, v))

ans = solve(n, links, queries)

print(('\n'.join(map(str, ans))))
