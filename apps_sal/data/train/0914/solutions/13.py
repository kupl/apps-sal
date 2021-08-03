from sys import stdin
t = int(stdin.readline())
while t:
    n, m = map(int, stdin.readline().split())
    a = []
    k = [[1 for _ in range(m)]for __ in range(n)]
    for _ in range(n):
        a.append(list(map(int, stdin.readline().split())))
    dp = [[a[i][_] for _ in range(m)]for i in range(n)]
    for i in range(1, n):
        for j in range(m):
            if j == m - 1:
                dp[i][j] = max(0, max(dp[i - 1][j - 1], dp[i - 1][j]))
            elif j == 0:
                dp[i][j] = max(0, max(dp[i - 1][j], dp[i - 1][j + 1]))

            else:
                dp[i][j] = max(0, max(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]))

            if dp[i][j] > a[i][j]:
                k[i][j] = 0
            else:
                k[i][j] = 1
                dp[i][j] = a[i][j]

    for i in range(n):
        for j in range(m):
            print(k[i][j], end='')
        print()

    t -= 1
