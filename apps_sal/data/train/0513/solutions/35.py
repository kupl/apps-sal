from bisect import bisect_left, bisect_right
import sys
sys.setrecursionlimit(10 ** 8)
N = int(input())
A = list(map(int, input().split()))
edge = [[] for _ in range(N)]
for i in range(N - 1):
    (a, b) = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)


def dfs(v, LIS):
    if len(edge[v]) == 0:
        return
    for u in edge[v]:
        if visited[u] == False:
            visited[u] = True
            if A[u] > LIS[-1]:
                LIS.append(A[u])
                ans[u] = len(LIS)
                dfs(u, LIS)
                LIS.pop()
            else:
                ind = bisect_left(LIS, A[u])
                stack = LIS[ind]
                LIS[ind] = A[u]
                ans[u] = len(LIS)
                dfs(u, LIS)
                LIS[ind] = stack
    return


ans = [0] * N
visited = [False] * N
visited[0] = True
LIS = [A[0]]
ans[0] = 1
dfs(0, LIS)
print(*ans, sep='\n')
