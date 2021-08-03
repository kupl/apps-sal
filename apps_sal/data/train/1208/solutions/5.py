fact = [0] * 1000009
dp = [0] * 1000009
fact[1] = 1
fact[2] = 2
dp[1] = 1
dp[2] = 2
mod = 1000000007
for i in range(3, 1000001):
    fact[i] = ((fact[i - 1] % mod) * (i % mod)) % mod
for i in range(3, 1000001):
    dp[i] = ((dp[i - 1] % mod) * (fact[i] % mod)) % mod
t = int(input())
for i in range(t):
    n = int(input())
    print(dp[n] % mod)
