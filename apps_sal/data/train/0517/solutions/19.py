factors = []


def fact(n):
    factors.clear()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i * i != n:
                factors.append(n // i)


(n, m) = map(int, input().split())
dp = [0] * (2 * 10 ** 5 + 1)
dp[2] = 2 % m
dp[3] = 6 % m
dp[4] = 12 % m
if n > 4:
    for i in range(5, n + 1):
        fact(i)
        k = (pow(2, i, m) - 2) % m
        if len(factors) == 0:
            dp[i] = k
        else:
            sub = 0
            for j in factors:
                sub += dp[j]
                sub %= m
            dp[i] = (k - sub) % m
print(dp[n])
