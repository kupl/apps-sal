def five_by_2n(n):
    def b(n):
        dp = [0] * n
        dp[:8] = [0, 8, 0, 95, 0, 1183, 0, 14824]
        for i in range(8, n):
            dp[i] = 15 * dp[i - 2] - 32 * dp[i - 4] + 15 * dp[i - 6] - dp[i - 8]
        return dp[-1] % 12345787
    if n<=8:
        return {1:8, 2:95, 3:1183, 4:14824, 5:185921, 6:2332097, 7:4561586,8:8916464}[n]
    else:
        return b(2*n)
