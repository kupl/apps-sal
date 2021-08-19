MOD = 10 ** 9 + 7


def power(x, n, MOD):
    ans = 1
    while n:
        if n % 2 == 1:
            ans = (ans * x) % MOD
        x = (x * x) % MOD
        n //= 2
    return ans


def getFacts(n, MOD):
    facts = [1] + [0] * n
    for x in range(1, n + 1):
        facts[x] = (facts[x - 1] * x) % MOD
    return facts


def getInvFacts(n, factN, MOD):
    invFacts = [0] * (n + 1)
    invFacts[n] = power(factN, MOD - 2, MOD)
    for x in reversed(list(range(n))):
        invFacts[x] = (invFacts[x + 1] * (x + 1)) % MOD
    return invFacts


def getInvss(B, D, facts, MOD):
    invss = [[0] * (D + 1) for _ in range(B + 1)]
    invss[B][D] = power(power(facts[B], D, MOD), MOD - 2, MOD)
    for i in reversed(list(range(B))):
        invss[i][D] = (invss[i + 1][D] * power(i + 1, D, MOD)) % MOD
    for i in range(B + 1):
        for k in reversed(list(range(D))):
            invss[i][k] = (invss[i][k + 1] * facts[i]) % MOD
    return invss


N, A, B, C, D = list(map(int, input().split()))

facts = getFacts(N, MOD)
invFacts = getInvFacts(N, facts[N], MOD)
invss = getInvss(B, D, facts, MOD)

# dp[i][j]: i人以下のグループのみで、j人使っている場合の数
dp = [[0] * (N + 1) for _ in range(B + 1)]
dp[A - 1][0] = 1

for i in range(A, B + 1):
    for j in range(N + 1):
        dp[i][j] = dp[i - 1][j]
        for k in range(C, min(D, j // i) + 1):
            dp[i][j] += facts[N - j + i * k] * invFacts[N - j] * invss[i][k] * invFacts[k] * dp[i - 1][j - i * k]
            dp[i][j] %= MOD

print((dp[B][N]))
