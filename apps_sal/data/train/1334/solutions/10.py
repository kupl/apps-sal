n = int(input())
supw = list(map(int, input().split()))
if len(supw) in [1, 2]:
    print(0)
elif len(supw) == 3:
    print(min(supw[0], min(supw[1], supw[2])))
else:
    dp = list()
    for i in range(1, len(supw) + 1):
        dp.append(0)
    dp[0] = supw[0]
    dp[1] = supw[1]
    dp[2] = supw[2]
    for i in range(3, len(supw)):
        dp[i] = supw[i] + min(dp[i - 1], min(dp[i - 2], dp[i - 3]))

    print(min(dp[n - 1], min(dp[n - 2], dp[n - 3])))
