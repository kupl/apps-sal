N = int(input())
s = len(input())
mod = 10 ** 9 + 7
dp = [1] + [0] * N
for i in range(N):
    dp = [dp[0] + dp[1]] + [(i + 2 * j) % mod for (i, j) in zip(dp[2:] + [0], dp[:-1])]
print(dp[s] * pow(2 ** s, mod - 2, mod) % mod)
