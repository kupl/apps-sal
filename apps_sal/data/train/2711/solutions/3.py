def outcome(n, s, k):

    if n * s * k == 0:
        return 0

    dp = [[0] * (k + 1) for i in range(n + 1)]

    for i in range(1, min(s + 1, k + 1)):
        dp[1][i] = 1

    for i in range(2, n + 1):
        for j in range(1, k + 1):
            for l in range(1, min(s + 1, j)):
                dp[i][j] += dp[i - 1][j - l]

    return dp.pop().pop()
