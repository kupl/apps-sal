def solve(n, m, aaa):
    s = sum(aaa)
    if s > m:
        return 0

    ms = m - s
    MOD = 10 ** 9 + 7

    f = 1
    for i in range(2, n + s + 1):
        f = f * i % MOD
    ans = pow(f, MOD - 2, MOD)

    for x in range(m + n, ms, -1):
        ans = ans * x % MOD

    return ans


n, m = list(map(int, input().split()))
aaa = list(map(int, input().split()))
print((solve(n, m, aaa)))
