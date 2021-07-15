MOD = 10 ** 9 + 7
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
r = n + sum(a)
m += n
if m < r:
    print((0))
else:
    ans = 1
    v = 1
    for i in range(r):
        v *= i + 1
        ans *= (m - i)
        v %= MOD
        ans %= MOD
    print((ans * pow(v, MOD - 2, MOD) % MOD))

