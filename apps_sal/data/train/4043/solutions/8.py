def calc(mp):
    h = len(mp)
    w = len(mp[0])
    dp = [[[0 for j in range(h + 1)]for i in range(h + 1)]for k in range(h + w + 1)]
    for s in range(1, h + w + 1):
        for i1 in range(1, h + 1):
            j1 = s - i1 + 1
            if j1 > 0 and j1 <= w:
                for i2 in range(1, h + 1):
                    j2 = s - i2 + 1
                    if j2 > 0 and j2 <= w:
                        dp[s][i1][i2] = max(dp[s - 1][i1][i2 - 1], dp[s - 1][i1 - 1][i2], dp[s - 1][i1 - 1][i2 - 1], dp[s - 1][i1][i2]) + mp[i1 - 1][j1 - 1] + mp[i2 - 1][j2 - 1]
                        if i1 == i2:
                            dp[s][i1][i2] -= mp[i1 - 1][j1 - 1]
    return dp[h + w - 1][h][h]
