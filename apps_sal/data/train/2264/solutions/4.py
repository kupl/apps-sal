import sys
from heapq import heappop, heappush


def main0(n, m, s, t, abc):
    mod = 10**9 + 7
    g = [set() for _ in range(n)]
    for i, (a, b, c) in enumerate(abc):
        a, b = a - 1, b - 1
        g[a].add((b, c, i))
        g[b].add((a, c, i))
    s, t = s - 1, t - 1
    todo = [[0, s]]
    inf = float('inf')
    froms = [inf] * n
    froms[s] = 0
    while todo:
        c, v = heappop(todo)
        if froms[v] < c:
            continue
        for nv, nc, _ in g[v]:
            if froms[nv] > c + nc:
                froms[nv] = c + nc
                heappush(todo, [nc + c, nv])
    mincost = froms[t]
    mideary = [0] * m
    midvary = [0] * n
    vary = [0] * n
    vary[t] = 1
    todo = [[0, t]]
    fromt = [inf] * n
    fromt[t] = 0
    fromt[s] = mincost
    while todo:
        c, v = heappop(todo)
        for nv, nc, i in g[v]:
            if mincost == froms[nv] + c + nc:
                if c < mincost / 2 and c + nc > mincost / 2:
                    mideary[i] += vary[v]
                    mideary[i] %= mod
                elif mincost % 2 == 0 and c + nc == mincost // 2:
                    midvary[nv] += vary[v]
                    midvary[nv] %= mod
                vary[nv] += vary[v]
                vary[nv] %= mod
                if fromt[nv] > c + nc:
                    fromt[nv] = c + nc
                    heappush(todo, [c + nc, nv])

    mideary1 = [0] * m
    midvary1 = [0] * n
    vary = [0] * n
    vary[s] = 1
    todo = [[0, s]]
    nfroms = [inf] * n
    nfroms[s] = 0
    nfroms[t] = mincost
    while todo:
        c, v = heappop(todo)
        for nv, nc, i in g[v]:
            if mincost == fromt[nv] + c + nc:
                if c < mincost / 2 and c + nc > mincost / 2:
                    mideary1[i] += vary[v]
                    mideary1[i] %= mod
                elif mincost % 2 == 0 and c + nc == mincost // 2:
                    midvary1[nv] += vary[v]
                    midvary1[nv] %= mod
                vary[nv] += vary[v]
                vary[nv] %= mod
                if nfroms[nv] > c + nc:
                    nfroms[nv] = c + nc
                    heappush(todo, [c + nc, nv])
    for i in range(n):
        midvary[i] *= midvary1[i]
        midvary[i] %= mod
    for i in range(m):
        mideary[i] *= mideary1[i]
        mideary[i] %= mod
    summid = sum(mideary) + sum(midvary)
    summid %= mod
    ret = 0
    for x in mideary:
        if x != 0:
            ret += x * (summid - x)
            ret %= mod
    for x in midvary:
        if x != 0:
            ret += x * (summid - x)
            ret %= mod
    return ret


input = sys.stdin.readline


def __starting_point():
    n, m = list(map(int, input().split()))
    s, t = list(map(int, input().split()))
    abc = [list(map(int, input().split())) for _ in range(m)]
    print((main0(n, m, s, t, abc)))


__starting_point()
