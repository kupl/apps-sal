n,m,lk = list(map(int,input().split()))
sp = [int(i)-1 for i in input().split()]
dp = []
for i in range(n):
 dp += [[0]*n]
for i in range(n):
 for j in range(n):
  if(i!=j):
   dp[i][j]=10**18
for _ in range(m):
 x,y,z = list(map(int,input().split()))
 dp[x-1][y-1]=z
 dp[y-1][x-1]=z
for k in range(n):
 for i in range(n):
  for j in range(n):
   if(dp[i][j]>dp[i][k]+dp[k][j]):
    dp[i][j]=dp[i][k]+dp[k][j]
dist = 10**18
for i in range(lk):
 for j in range(i+1,lk):
  dist = min(dist,dp[sp[i]][sp[j]])
print(dist)

