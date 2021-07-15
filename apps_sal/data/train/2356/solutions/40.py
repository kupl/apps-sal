n,k=map(int,input().split())
dp=[[0]*(2*n+1) for _ in range(n+1)]
dp[0][0]=1
mod=998244353
for i in range(1,n+1):
    for j in reversed(range(n+1)):
        dp[i][j]+=dp[i][2*j]
        if j>0:
            dp[i][j]+=dp[i-1][j-1]
        dp[i][j]%=mod
print(dp[n][k])
