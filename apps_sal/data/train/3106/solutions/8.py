def makec():
    dp = [[-1] * 801 for _ in range(801)]
    for n in range(801):
        dp[n][n] = 1
        dp[n][1] = 1
        dp[n][0] = 0

    def c(n, k):
        if k > n:
            return 0
        if dp[n][k] < 0:
            dp[n][k] = k * c(n - 1, k) + c(n - 1, k - 1)
        return dp[n][k]
    return c


c = makec()


def combs_non_empty_boxes(n, k):
    if k > n:
        combs = 'It cannot be possible!'
    else:
        combs = c(n, k)
    return combs
