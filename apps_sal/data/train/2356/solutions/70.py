(N, K) = list(map(int, input().split()))
P = 998244353
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    for k in range(N, 0, -1):
        if 2 * k <= N:
            dp[i][k] = (dp[i - 1][k - 1] + dp[i][2 * k]) % P
        else:
            dp[i][k] = dp[i - 1][k - 1]
print(dp[N][K])
