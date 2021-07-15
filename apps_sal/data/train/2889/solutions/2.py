def count_ways(n, k):
    dp = []
    for i in range(k):
        dp.append(2 ** i)
    for i in range(k, n):
        dp.append(sum(dp[-k:]))
    return dp[~-n]
