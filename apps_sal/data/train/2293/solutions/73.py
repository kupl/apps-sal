import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp = [[A[S], 0] for S in range(1 << N)]
for k in range(N):
    for S in range(1 << N):
        if S >> k & 1:
            if dp[S][0] < dp[S ^ 1 << k][0]:
                dp[S][1] = max(dp[S][0], dp[S ^ 1 << k][1])
                dp[S][0] = dp[S ^ 1 << k][0]
            else:
                dp[S][1] = max(dp[S][1], dp[S ^ 1 << k][0])
ans = 0
for K in range(1, 1 << N):
    ans = max(ans, sum(dp[K]))
    print(ans)
