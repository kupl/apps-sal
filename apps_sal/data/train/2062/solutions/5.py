def prepare(n, MOD):
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f = f * m % MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv = inv * m % MOD
        invs[m - 1] = inv

    return factorials, invs


def solve(n, a, b, c, d, MOD):
    facts, invs = prepare(n, MOD)

    pre = {}
    for i in range(a, b + 1):
        iv = invs[i]
        for k in range(c, d + 1):
            if i * k > n:
                break
            pre[i, k] = pow(iv, k, MOD) * invs[k] % MOD

    dp = [0] * (n + 1)
    dp[n] = 1
    for i in range(a, b + 1):
        iv = invs[i]
        for j in range(i * c, n + 1):
            base = dp[j]
            for k in range(c, d + 1):
                ik = i * k
                if ik > j:
                    break
                dp[j - ik] = (dp[j - ik] + base * pre[i, k]) % MOD
    return dp[0] * facts[n] % MOD


n, a, b, c, d = list(map(int, input().split()))
MOD = 10 ** 9 + 7
print((solve(n, a, b, c, d, MOD)))
