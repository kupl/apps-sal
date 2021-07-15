n,k=map(int,input().split())
dp=[[0 for j in range(3001)] for i in range(n+1)]

for i in range(1, n+1):
  for j in range(3000, -1, -1):
    if i < j or j == 0:
      dp[i][j] = 0
    elif i == j:
      dp[i][j] = 1
    else:
      dp[i][j] = (dp[i-1][j-1] + (0 if i < j*2 else dp[i][j*2])) % 998244353

print(dp[n][k])
