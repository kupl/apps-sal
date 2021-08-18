from sys import stdin
from math import ceil, gcd


def dfs(src, visit):
    visit[src] = 1
    for nbr in d[src]:
        if visit[nbr] == 0:
            dfs(nbr, visit)


for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    d = {}
    for i in range(m):
        u, v = list(map(int, stdin.readline().split()))
        if u in d:
            d[u].append(v)
        else:
            d[u] = [v]
        if v in d:
            d[v].append(u)
        else:
            d[v] = [u]
    visited = {}
    for i in range(n):
        visited[i] = 0
    ans = 0
    for i in range(n):
        if visited[i] == 0:
            ans += 1
            if i in d:
                dfs(i, visited)
    print(ans)
