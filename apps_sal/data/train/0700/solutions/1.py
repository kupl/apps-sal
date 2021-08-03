for t in range(eval(input())):
    dp = [[0 for i in range(4)] for j in range(2)]
    ret = 1
    for u in range(eval(input())):
        c = list(map(int, input().split()))
        for i in range(4):
            dp[u & 1][i] = 1e18
            for j in range(4):
                if j != i:
                    dp[u & 1][i] = min(dp[u & 1][i], c[j] + dp[1 - (u & 1)][j])
                    ret = min(dp[u & 1])
    print(ret)
