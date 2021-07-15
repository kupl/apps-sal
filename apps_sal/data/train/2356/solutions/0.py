n,k=map(int,input().split())
mod=998244353
dp=[0]*(n+1)
dp[0]=1
for i in range(1,n+1):
  for j in range(i,-1,-1):
    dp[j]=dp[j-1]
    if 2*j<=i:
      dp[j]+=dp[2*j]
    dp[j]%=mod
print(dp[k])
