from sys import stdin
import sys

sys.setrecursionlimit(10**6)

N, M = list(map(int, stdin.readline().split()))

g = [[] for i in range(0, N)]

for i in range(0, M):
    a, b, c = list(map(int, stdin.readline().split()))
    a -= 1
    b -= 1
    g[a].append((b, c))
    g[b].append((a, c))

vis = [False] * N
col = [-1] * N


def dfs(v):
    nonlocal vis
    nonlocal col
    vis[v] = True

    for to, c in g[v]:
        if vis[to] == True:
            continue
        if c == col[v]:
            if c == 1:
                col[to] = 2
            else:
                col[to] = 1
        else:
            col[to] = c

        dfs(to)


col[0] = 1
dfs(0)

for i in range(0, N):
    print((col[i]))
