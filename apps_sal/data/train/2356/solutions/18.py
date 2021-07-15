import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
mod = 998244353

dp = [[0]*(N*2+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    for j in range(N, 0, -1):
        # j-1 の i-1 分割に 1 を足す + 2*j の i 分割を 2 で割る
        dp[i][j] = (dp[i-1][j-1] + dp[i][2*j])%mod

print(dp[N][K]%mod)
