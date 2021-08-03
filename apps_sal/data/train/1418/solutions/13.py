for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    k = n + 1
    dp = [0] * k
    dp[1] = a[0]

    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1] + a[i - 1] * i, dp[i - 2] + a[i - 2] * i + a[i - 1] * (i - 1))

    print(dp[n])
