def target_game(values):
    n = len(values)
    dp = [0] * (n + 1)
    dp[1] = values[0] if values[0] > 0 else 0
    for ind in range(2, n + 1):
        dont_take = dp[ind - 1]
        take = dp[ind - 2] + values[ind - 1] if values[ind - 1] > 0 else dp[ind - 2]
        dp[ind] = max(dont_take, take)
    return dp[n]
