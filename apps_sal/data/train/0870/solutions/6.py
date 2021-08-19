t = int(input())
while t > 0:
    st = input()
    dp = [0 if i < 2 else len(st) for i in range(6)]
    for c in st:
        if c == '1':
            dp[3] = min(dp[3], dp[1])
            dp[1] += 1
            dp[4] = min(dp[4], dp[2])
            dp[2] += 1
            dp[5] += 1
        else:
            dp[2] = min(dp[2], dp[0])
            dp[0] += 1
            dp[5] = min(dp[5], dp[3])
            dp[3] += 1
            dp[4] += 1
    print(min(dp))
    t = t - 1
