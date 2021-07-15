for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[[None, None], [None, None]] for _ in range(n)]
    dp[n-1] = [[1,2], [1,2]]
    i = n-2
    while i > -1:
        if a[i+1] > a[i]:
            dp[i][1][0] = 1 + dp[i+1][0][0]
            dp[i][1][1] = 1 + dp[i+1][0][1]
            dp[i][0][1] = 2 + dp[i+1][0][0]
            dp[i][0][0] = 1
        elif a[i+1] < a[i]:
            dp[i][0][1] = 1 + dp[i+1][1][1]
            dp[i][0][0] = 1 + dp[i+1][1][0]
            dp[i][1][1] = 2 + dp[i+1][1][0]
            dp[i][1][0] = 1
        else:
            dp[i][1][0] = 1 + dp[i+1][0][0]
            dp[i][1][1] = 1 + dp[i+1][0][1]
            dp[i][0][1] = 1 + dp[i+1][1][1]
            dp[i][0][0] = 1 + dp[i+1][1][0]
        i -= 1
    print(max([dp[p][1][1] for p in range(n)]))

