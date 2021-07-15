import sys
sys.setrecursionlimit(10**9)
N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((v, c))
    edges[v].append((u, c))

ans = [-1] * N
ans[0] = 1

def dfs(u):
    for v, c in edges[u]:
        if ans[v] != -1: continue
        if ans[u] == c: 
            if c == 1:
                ans[v] = 2
            else:
                ans[v] = 1
        else: 
            ans[v] = c
        dfs(v)

dfs(0)
print(*ans, sep="\n")
