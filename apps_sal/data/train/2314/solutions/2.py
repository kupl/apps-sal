# t=int(input())
t = 1
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    dp = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        dp[0][i] = l[i]
    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = dp[i - 1][j] ^ dp[i - 1][j + 1]

    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j + 1])

    q = int(input())
    for __ in range(q):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        print(dp[y - x][x])
