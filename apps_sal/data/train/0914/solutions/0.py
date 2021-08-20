try:
    t = int(input())
    while t > 0:
        t -= 1
        (n, m) = list(map(int, input().split()))
        a = [list(map(int, input().split())) for _ in range(n)]
        dp = [[0 for _ in range(m)] for _ in range(n)]
        ans = [['0' for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i - 1 < n:
                    if 0 <= j - 1 and j + 1 < m:
                        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])
                    elif j == 0:
                        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + 1])
                    elif j == m - 1:
                        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])
                if dp[i][j] > a[i][j]:
                    ans[i][j] = '0'
                else:
                    ans[i][j] = '1'
                    dp[i][j] = a[i][j]
        for i in ans:
            print(''.join(i))
except:
    pass
