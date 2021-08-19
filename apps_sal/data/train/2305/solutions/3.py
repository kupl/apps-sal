import sys
readline = sys.stdin.readline


def parorder(Edge, p):
    N = len(Edge)
    par = [0] * N
    par[p] = -1
    stack = [p]
    order = []
    visited = set([p])
    ast = stack.append
    apo = order.append
    while stack:
        vn = stack.pop()
        apo(vn)
        for vf in Edge[vn]:
            if vf in visited:
                continue
            visited.add(vf)
            par[vf] = vn
            ast(vf)
    return (par, order)


def getcld(p):
    res = [[] for _ in range(len(p))]
    for (i, v) in enumerate(p[1:], 1):
        res[v].append(i)
    return res


def dfs(St):
    dist = [0] * N
    stack = St[:]
    used = [False] * N
    for s in St:
        used[s] = True
    while stack:
        vn = stack.pop()
        for vf in Edge[vn]:
            if not used[vf]:
                used[vf] = True
                dist[vf] = 1 + dist[vn]
                stack.append(vf)
    return dist


N = int(readline())
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    (a, b) = map(int, readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
dist0 = dfs([0])
fs = dist0.index(max(dist0))
distfs = dfs([fs])
en = distfs.index(max(distfs))
disten = dfs([en])
Dia = distfs[en]
path = []
for i in range(N):
    if distfs[i] + disten[i] == Dia:
        path.append(i)
if max(dfs(path)) > 1:
    print(-1)
else:
    path.sort(key=lambda x: distfs[x])
    cnt = 1
    hold = 0
    perm1 = [None] * N
    onpath = set(path)
    idx = 0
    for i in range(Dia + 1):
        vn = path[i]
        hold = 0
        for vf in Edge[vn]:
            if vf in onpath:
                continue
            hold += 1
            perm1[idx] = cnt + hold
            idx += 1
        perm1[idx] = cnt
        idx += 1
        cnt = cnt + hold + 1
    cnt = 1
    hold = 0
    perm2 = [None] * N
    onpath = set(path)
    idx = 0
    for i in range(Dia + 1):
        vn = path[Dia - i]
        hold = 0
        for vf in Edge[vn]:
            if vf in onpath:
                continue
            hold += 1
            perm2[idx] = cnt + hold
            idx += 1
        perm2[idx] = cnt
        idx += 1
        cnt = cnt + hold + 1
    print(*min(perm1, perm2))
