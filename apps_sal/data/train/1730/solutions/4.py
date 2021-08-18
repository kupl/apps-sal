def two_by_n(n, k):
    dp = [[0 for i in range(2)] for j in range(n + 1)]
    dp[1][0] = k
    if n < 2:
        print("here")
        return sum(dp[-1])
    dp[2] = [k * (k - 1), k * (k - 1)]
    NUM = 12345787
    for i in range(3, n + 1):
        dp[i][0] = (max(k - 1, 0) * dp[i - 1][0] + max(k - 2, 0) * dp[i - 1][1]) % NUM
        dp[i][1] = (max(k - 1, 0) * max(k - 2, 0) * dp[i - 2][0] + (max(k - 1, 0) + max(k - 2, 0) * max(k - 2, 0)) * dp[i - 2][1]) % NUM
    return sum(dp[-1]) % NUM
