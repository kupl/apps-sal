import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LI2(): return list(map(int, sys.stdin.readline().rstrip()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def LS2(): return list(sys.stdin.readline().rstrip())


N, K = MI()
mod = 998244353

dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    for j in range(N, 0, -1):
        dp[i][j] = dp[i - 1][j - 1]
        if 2 * j <= N:
            dp[i][j] += dp[i][2 * j]
            dp[i][j] %= mod
print((dp[-1][K]))
