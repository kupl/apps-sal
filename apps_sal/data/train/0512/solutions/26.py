import sys
sys.setrecursionlimit(10**6 + 1)


def input():
    x = sys.stdin.readline()
    return x[:-1] if x[-1] == "\n" else x


def printe(*x): print("
def printl(li): _ = print(*li, sep="\n") if li else None


N, Q=map(int, input().split())

edge=[[] for i in range(N)]
for i in range(N - 1):
    a, b, c, w=map(int, input().split())
    edge[a - 1].append((b - 1, c - 1, w))
    edge[b - 1].append((a - 1, c - 1, w))


def dfs(start):
    q = [(start, -1, 0, 0)]
    pars = [-1] * N
    depth = [-1] * N
    dist = [-1] * N
    while len(q):
        e, p, d, dis=q.pop()
        if depth[e] != -1:
            continue
        pars[e] = p
        depth[e] = d
        dist[e] = dis
        for ne, c, w in edge[e]:
            q.append((ne, e, d + 1, dis + w))
    return pars, depth, dist


pars, d, dist=dfs(0)
ln=N.bit_length()
dp=[[-1] * N for _ in range(ln + 1)]
dp[0]=pars
for i in range(1, ln + 1):
    for j in range(N):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]


def lca(u, v):
    du = d[u]
    dv = d[v]
    if du > dv:
        du, dv=dv, du
        u, v=v, u
    dif=dv - du
    for i in range(ln + 1):
        if (dif >> i) & 1:
            v = dp[i][v]
    if u == v:
        return u
    for i in range(ln, -1, -1):
        pu = dp[i][u]
        pv = dp[i][v]
        if pu != pv:
            u, v=pu, pv
    return pars[u]


q=Q
qs=tuple(tuple(map(int, input().split())) for i in range(Q))
ans=[0] * Q
qn=[[] for _ in range(N)]
for i, (x, y, u, v) in enumerate(qs):
    ans[i] = dist[u - 1] + dist[v - 1] - 2 * dist[lca(u - 1, v - 1)]
    qn[u - 1].append((i, x - 1, y, 1))
    qn[v - 1].append((i, x - 1, y, 1))
    qn[lca(u - 1, v - 1)].append((i, x - 1, y, -2))

cc = [[0, 0] for _ in range(N - 1)]

dfq = [(0, None, 0, -1)]


def dfs2(e, c, d, p):
    if c != None:
        cc[c][0] += 1
        cc[c][1] += d
    for qi, x, y, sgn in qn[e]:
        ans[qi] += (y * cc[x][0] - cc[x][1]) * sgn
    for ne, nc, nd in edge[e]:
        if ne == pars[e]:
            continue
        dfs2(ne, nc, nd, e)
    if c != None:
        cc[c][0] -= 1
        cc[c][1] -= d


dfs2(0, -1, 0, None)
printl(ans)
