N,K = map(int,input().split())
dp = [[0]*n for n in range(1,N+2)]
for n in range(N+1):
    dp[n][n] = 1
    for k in reversed(range(1,n)):
        if 2*k <= n:
            dp[n][k] = (dp[n-1][k-1] + dp[n][2*k])% 998244353
        else:
            dp[n][k] = dp[n-1][k-1]
    dp[n][0] = 0
#    print(dp)
print(dp[N][K])
