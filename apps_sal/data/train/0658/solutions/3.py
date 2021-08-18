t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    dp = [[1] * 2 for _ in range(n)]

    for i in range(n - 2, -1, -1):
        if a[i] <= a[i + 1]:
            dp[i][0] = 1 + dp[i + 1][1]

        if a[i] >= a[i + 1]:
            dp[i][1] = 1 + dp[i + 1][0]

    m = 0
    for i in range(n):
        l = dp[i][0]
        if l % 2 == 0:
            m = max(m, l + dp[i + l - 1][0])
        else:
            m = max(m, l + dp[i + l - 1][1])

    print(m)
