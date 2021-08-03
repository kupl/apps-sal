def main():
    mod = 998244353
    n, k = list(map(int, input().split()))
    dp = [[0] * (n + 1) for _ in [0] * (n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(n, 0, -1):
            if 2 * j <= n:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i][2 * j]) % mod
            else:
                dp[i][j] = dp[i - 1][j - 1]

    print((dp[n][k]))


main()
