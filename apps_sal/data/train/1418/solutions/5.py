for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    dp = [0 for i in range(n + 1)]
    dp[1] = l[0]
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1] + i * l[i - 1], dp[i - 2] + i * l[i - 2] + (i - 1) * l[i - 1])
    print(dp[n])
