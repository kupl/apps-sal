import sys


def dfs(adj, n):
    vis[n] = True
    for i in adj[n]:
        if vis[i] == False:
            dfs(adj, i)


sys.setrecursionlimit(10 ** 9)
(n, k) = map(int, input().split())
a = []
for i in range(n):
    t = list(map(int, input().split()))
    a.append(t[1:])
adj = []
global vis
vis = [False] * n
for i in range(n):
    adj.append([])
for i in range(n):
    for j in range(i + 1, n):
        c = len(set(a[i]).intersection(set(a[j])))
        if c >= k:
            adj[i].append(j)
            adj[j].append(i)
dfs(adj, 0)
c = 0
for i in range(0, n):
    if vis[i] == True:
        c += 1
print(c)
