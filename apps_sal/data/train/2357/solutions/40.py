MOD = 10 ** 9 + 7
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
ans = 1
den = 1
for i in range(s + n):
    ans *= m + n - i
    ans %= MOD
    den *= i + 1
    den %= MOD
ans = ans * pow(den, MOD - 2, MOD) % MOD
print(ans)
