import sys
import bisect


MAX_N = 200005
INF = 10**9 + 5

sys.setrecursionlimit(MAX_N)

N = int(sys.stdin.readline())
A = [int(x) for x in sys.stdin.readline().split()]
E = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    E[u - 1].append(v - 1)
    E[v - 1].append(u - 1)

lis = [INF] * N
ans = [0] * N


def dfs(u, r=-1):

    i = bisect.bisect_left(lis, A[u])
    old = lis[i]
    lis[i] = A[u]

    for v in E[u]:
        if v == r:
            continue

        dfs(v, u)

    ans[u] = bisect.bisect_left(lis, INF - 1)
    lis[i] = old


dfs(0)
for i in range(N):
    print(ans[i])
