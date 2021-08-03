N, K = list(map(int, input().split()))
C = 998244353

dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    for j in range(N, 0, -1):
        if j > i:
            continue
        dp[i][j] = dp[i - 1][j - 1]
        if 2 * j <= N:
            dp[i][j] = (dp[i][j] + dp[i][2 * j]) % C
print((dp[N][K]))
