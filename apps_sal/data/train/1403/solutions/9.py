for _ in range(int(input())):
    s = input()
    n = len(s)
    dp = [0 for _ in range(n)]
    if s[0] != '0':
        dp[0] = 1
    for i in range(1, n):
        x = int(s[i])
        y = int(s[i - 1:i + 1])
        if x >= 1 and x <= 9:
            dp[i] += dp[i - 1]
        if y >= 10 and y <= 26:
            if i - 2 >= 0:
                dp[i] += dp[i - 2]
            else:
                dp[i] += 1
    print(dp[-1] % 1000000007)
