

dp = [-1 for i in range(11919)]
fac = [1 for i in range(111)]
for i in range(1, 100):
    fac[i] = fac[i - 1] * i


def comb(n, r):
    return fac[n] / (fac[n - r] * fac[r])
    ret = 1
    for i in range(r):
        ret *= (n - i)
        ret /= (i + 1)
    return ret


def solve(n):
    if dp[n] > 0:
        return dp[n]
    if n == 0:
        return 1
    ans = 0
    for i in range(n):
        ans += comb(n - 1, i) * solve(i) * pow(2, n - 1 - i) * fac[(n - 1 - i)]
    dp[n] = ans
    return dp[n]


t = int(input())
for i in range(t):
    n = int(input())
    ans = 0
    for i in range(n):
        ans += comb(n - 1, i) * solve(i) * pow(2, n - 1 - i) * fac[(n - 1 - i)]
    print(ans)
