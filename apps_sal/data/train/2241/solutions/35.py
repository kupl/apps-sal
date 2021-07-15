import sys
input = sys.stdin.readline
import numpy as np
MOD = 10**9+7

n, c = map(int, input().split())
A = np.array(tuple(map(int, input().split())))
B = np.array(tuple(map(int, input().split())))
E = np.zeros((n, c+1), dtype=np.int64)
for j in range(c+1):
  cum = np.array(tuple(pow(k, j, MOD) for k in range(401))).cumsum()%MOD
  E[:, j] = cum[B] - cum[A-1]

dp = np.zeros((n+1, c+1), dtype=np.int64)
dp[0, 0] = 1
for i, e in enumerate(E):
  for j, f in enumerate(e):
    dp[i+1, j:] += dp[i, :c+1-j]*f
    dp[i+1, j:] %= MOD
ans = dp[n, c]
print(ans)
