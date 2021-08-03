def ans(n, k):
    dp = [[0 for x in range(6001)]for y in range(6001)]
    dp[1][1] = 1
    for i in range(2, n + 1):
        for j in range(3000, 0, -1):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i][2 * j]) % 998244353
    print(dp[n][k])


n, k = (int(x) for x in input().split())
ans(n, k)
