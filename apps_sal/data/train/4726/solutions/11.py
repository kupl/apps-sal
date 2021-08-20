def solve(s):
    n = len(s)
    (dp, mod, sum) = ([0] * n, 1000000007, 0)
    for i in range(n - 2, -1, -1):
        dp[i] = (dp[i + 1] * 26 % mod + (ord('Z') - ord(s[i + 1])) % mod) % mod
    for i in range(0, n):
        sum += (dp[i] + 1) * (ord('Z') - ord(s[i])) % mod
        sum %= mod
    return sum
