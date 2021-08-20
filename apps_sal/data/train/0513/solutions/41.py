from bisect import bisect_left
import sys
sys.setrecursionlimit(10 ** 9)
N = int(input())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(N - 1):
    (u, v) = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
root = 0
stack = [root]
visited = set()
visited.add(root)
done = set()
vs = []
ans = [0] * N
memo = [None] * N
memo[root] = (0, A[root])
INF = 10 ** 10
dp = [INF] * N
while stack:
    now_ = stack[-1]
    if now_ in done:
        (j, a) = memo[now_]
        dp[j] = a
        stack.pop()
        vs.append(now_)
    else:
        for next_ in G[now_][::-1]:
            if next_ in visited:
                continue
            visited.add(next_)
            stack.append(next_)
        done.add(now_)
        tmp = bisect_left(dp, A[now_])
        memo[now_] = (tmp, dp[tmp])
        dp[tmp] = A[now_]
        ans[now_] = bisect_left(dp, INF)
print(*ans, sep='\n')
