def count_subsequences(sub,s):
    dp = [[0]*(len(s)+1) for _ in range(len(sub))]
    dp.append([1]*len(s))
    for x,c in enumerate(sub):
        for y,v in enumerate(s):
            dp[x][y] = dp[x][y-1] + dp[x-1][y-1] * (c==v)
    return dp[-2][-2]
