t = int(input())
for i in range(t):
    (n, m) = map(int, input().split())
    arr = []
    for j in range(n):
        arr += [[int(j) for j in input().split()]]
    dp = [[0 for i in range(m)] for j in range(n)]
    ans = [[0 for i in range(m)] for j in range(n)]
    for i in range(m):
        dp[0][i] = arr[0][i]
        ans[0][i] = 1
    if m == 1:
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], arr[i][0])
            if dp[i][0] == arr[i][0]:
                ans[i][0] = 1
        for x in ans:
            print(*x, sep='')
        continue
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], arr[i][0])
        if dp[i][0] == arr[i][0]:
            ans[i][0] = 1
        for j in range(1, m - 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1], arr[i][j])
            if dp[i][j] == arr[i][j]:
                ans[i][j] = 1
        dp[i][m - 1] = max(dp[i - 1][m - 1], dp[i - 1][m - 2], arr[i][m - 1])
        if dp[i][m - 1] == arr[i][m - 1]:
            ans[i][m - 1] = 1
    for x in ans:
        print(*x, sep='')
