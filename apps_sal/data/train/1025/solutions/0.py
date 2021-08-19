from collections import defaultdict as dd, deque as dq


def opbfs(u, vis, ll, parr):
    q = dq([(u, 0)])
    uu = u
    su = 0
    while q:
        (u, lol) = q.pop()
        par = parr[u]
        if lol % 2 == 0:
            vis[u] = 1
            su += ll[u - 1]
            ll[u - 1] = 0
        for j in d[u]:
            if j != par:
                q.appendleft((j, lol + 1))
    ll[uu - 1] = su


def bfs(height, d, parr):
    q = dq([1])
    while q:
        u = q.pop()
        height[u] = height[parr[u]] + 1
        for i in d[u]:
            if i != parr[u]:
                q.appendleft(i)
                parr[i] = u


t = int(input())
while t:
    (n, q) = map(int, input().split())
    ll = list(map(int, input().split()))
    d = dd(list)
    for i in range(n - 1):
        (u, v) = map(int, input().split())
        d[u].append(v)
        d[v].append(u)
    vis = [0] * (n + 1)
    l = []
    height = [0] * (n + 1)
    parr = [0] * (n + 1)
    bfs(height, d, parr)
    for i in range(q):
        u = int(input())
        l.append((height[u], u, i))
    l.sort()
    vis = [0] * (n + 1)
    for i in l:
        (he, u, ind) = i
        if vis[u] == 0:
            opbfs(u, vis, ll, parr)
    print(*ll)
    t -= 1
