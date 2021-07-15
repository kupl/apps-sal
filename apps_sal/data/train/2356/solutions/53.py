N, K = map(int, input().split())
mod = 998244353
dp = [[0]*(N+1) for _ in range(N+1)]

dp[1][1] = 1

for n in range(2,N+1):
  for k in range(n,0,-1):
    if 2*k <= n:
      dp[n][k] = (dp[n-1][k-1] + dp[n][2*k]) % mod
    else:
      dp[n][k] = dp[n-1][k-1] % mod
      
print(dp[N][K])
