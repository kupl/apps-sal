import sys

sys.setrecursionlimit(10**6)

def dfs(now):
    for nxt, color in edge[now]:
        if res[nxt] == 0:
            if res[now] == color:
                res[nxt] = (color + 1 if color < n else 1)
            else:
                res[nxt] = color
        
            dfs(nxt)
    
    return


n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    edge[u-1].append([v-1, c])
    edge[v-1].append([u-1, c])

res = [0] * n
res[0] = 1

dfs(0)

print(*res, sep='\n')
