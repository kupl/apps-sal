def calc(cards):
    f = 1 << len(cards)
    dp = [f * v for v in cards]
    for d in range(1, len(cards)):
        f >>= 1
        dp = [max(dp[i] + f * cards[i + d], dp[i + 1] + f * cards[i])
              for i in range(len(dp) - 1)]
    return dp.pop()
