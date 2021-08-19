import sys


def N():
    return int(input())


def NM():
    return map(int, input().split())


def L():
    return list(NM())


def LN(n):
    return [N() for i in range(n)]


def LL(n):
    return [L() for i in range(n)]


n = N()
edge = [[] for i in range(n + 1)]
for i in range(n - 1):
    (a, b) = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
INF = float('inf')
ma = [INF] * (n + 1)
mi = [-INF] * (n + 1)
k = N()
vp = LL(k)
for (v, p) in vp:
    ma[v] = p
    mi[v] = p
sys.setrecursionlimit(10 ** 6)


def dfs(v, d, hi, lo):
    dep[v] = d
    ma[v] = min(ma[v], hi)
    mi[v] = max(mi[v], lo)
    hi = ma[v]
    lo = mi[v]
    for i in edge[v]:
        if dep[i] == -1:
            (hi, lo) = dfs(i, d + 1, hi + 1, lo - 1)
            ma[v] = min(ma[v], hi)
            mi[v] = max(mi[v], lo)
            hi = ma[v]
            lo = mi[v]
    return (hi + 1, lo - 1)


for i in range(2):
    dep = [-1 for i in range(n + 1)]
    dfs(v, 0, p, p)
for (i, j) in zip(mi, ma):
    if i > j or (i - j) % 2 == 1:
        print('No')
        break
else:
    print('Yes')
    for i in mi[1:]:
        print(i)
