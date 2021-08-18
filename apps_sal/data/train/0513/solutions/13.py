from bisect import bisect_left
import sys
readline = sys.stdin.readline
read = sys.stdin.read

N = int(input())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = list(map(int, input().split()))
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

INF = 10**9 + 1

q = [0]
dp = [INF] * N
ans = [0] * N
lis_len = 0
idx = [-1] * N
old = [-1] * N
prev = [-1] * N

ss = 0
while q:
    now = q.pop()
    if now >= 0:
        a = A[now]
        idx[now] = bisect_left(dp, a)
        iv = idx[now]
        old[now] = dp[idx[now]]
        x = old[now]
        if x == INF:
            lis_len += 1
        dp[iv] = a
        ans[now] = lis_len

        for nxt in G[now]:
            if nxt == prev[now]:
                continue
            prev[nxt] = now
            q.append((-1) * nxt)
            q.append(nxt)
    else:
        now = (-1) * now
        dp[idx[now]] = old[now]
        x = dp[idx[now]]
        if x == INF:
            lis_len -= 1

for a in ans:
    print(a)
