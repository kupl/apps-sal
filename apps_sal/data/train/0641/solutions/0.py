n = int(input())
cost = []
d = {}
val_desc = [0] * n
visited = set()
visited.add(0)
dfstack = []
desc = [[False for i in range(n)] for i in range(n)]
for i in range(n):
    cost.append(int(input()))
    d[i] = []

for i in range(n - 1):
    j, k = list(map(int, input().split()))
    d[j - 1].append(k - 1)
    d[k - 1].append(j - 1)


def dfs(u):
    val_desc[u] += cost[u]
    dfstack.append(u)
    for i in dfstack:
        desc[u][i] = True
    for i in d[u]:
        if i not in visited:
            visited.add(i)
            dfs(i)
            val_desc[u] += val_desc[i]
    dfstack.pop(-1)


dfs(0)
mp = 10**9
coco = sum(cost)
for i in range(n):
    for j in range(i + 1, n):
        vali = val_desc[i]
        valj = val_desc[j]
        if desc[i][j]:
            valj -= val_desc[i]
        if desc[j][i]:
            vali -= val_desc[j]
        p = max(vali, valj, coco - vali - valj)
        mp = min(mp, p)
print(mp)
