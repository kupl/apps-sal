N, K = map(int, input().split())
MOD = 998244353
dp = [[0]*(N+1) for _ in range(N+1)]
dp[1][1] = 1

def get_dp(n, k):
    try:
        return dp[n][k]
    except:
        return 0


for n in range(2, N+1):
    for k in range(n, -1, -1):
        dp[n][k] = get_dp(n-1, k-1) + get_dp(n, 2*k)
        dp[n][k] %= MOD

print(dp[N][K])
