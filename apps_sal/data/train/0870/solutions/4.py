for _ in range(int(input())):
    s = str(input())
    dp = [0, 0, len(s), len(s), len(s), len(s)]
    for i in s:
        if i == '1':
            dp[3] = min(dp[3], dp[0])
            dp[0] += 1
            dp[5] = min(dp[5], dp[2])
            dp[2] += 1
            dp[4] += 1
        else:
            dp[2] = min(dp[2], dp[1])
            dp[1] += 1
            dp[4] = min(dp[4], dp[3])
            dp[3] += 1
            dp[5] += 1
    print(min(dp))
