def dfs(v, col):
    used[v] = col
    for u in g[v]:
        if used[u] == -1:
            dfs(u, col ^ 1)

n = int(input())
used = [1 for i in range(n)]
for i in range(2, n + 2):
    if used[i - 2] == 1:
        for j in range(i * i, n + 2, i):
            used[j - 2] = 2
print(max(used))
print(*used)

