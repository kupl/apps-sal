def resolve():
  mod = 998244353
  N, K = list(map(int, input().split(" ")))

  # dp = [[0]*(K+1) for _ in range(N+1)]
  dp = [[0]*(N+1) for _ in range(N+1)]
  for n in range(N+1):
    dp[n][n] = 1

  for n in range(1, N+1):
    for k in range(n, 0, -1):
      result = dp[n-1][k-1]
      if 2*k <= n: result += dp[n][2*k]
      dp[n][k] = result%mod if result > mod else result
  
  print((dp[N][K]))

def __starting_point():
  resolve()

__starting_point()
