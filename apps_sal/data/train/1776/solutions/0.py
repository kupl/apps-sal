def roll_dice (rolls, sides, threshold):
    dp = [0] * (rolls * sides + 1)
    for i in range(1, sides+1):
        dp[i] = 1

    for _ in range(rolls-1):
        for x in range((rolls * sides), 0, -1):
            dp[x] = sum(dp[max(1, x-sides):x])

    return sum(dp[threshold:]) / sum(dp[1:])
