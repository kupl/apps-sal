MOD = 10 ** 9 + 7
(n, m) = [int(item) for item in input().split()]
a = [int(item) for item in input().split()]
b = [int(item) for item in input().split()]
cumsum = [[1] * 410 for _ in range(410)]
for order in range(405):
    for i in range(1, 405):
        cumsum[order][i] = pow(i, order, MOD) + cumsum[order][i - 1]
        cumsum[order][i] %= MOD
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(0, m + 1):
        for k in range(j + 1):
            l = a[i - 1]
            r = b[i - 1]
            x = (cumsum[j - k][r] - cumsum[j - k][l - 1] + MOD) % MOD
            dp[i][j] += dp[i - 1][k] * x
        dp[i][j] %= MOD
print(dp[-1][-1])
