MOD = 10 ** 9 + 7
p = 100000
fact = [0] * p
fact[0] = 1
for i in range(1, p):
    fact[i] = fact[i - 1] * i % MOD


def MI(a, MOD):
    return pow(a, MOD - 2, MOD)


def nck(n, k):
    if n == k or k == 0:
        return 1
    if n < k:
        return 0
    return fact[n] * MI(fact[k], MOD) % MOD * MI(fact[n - k], MOD) % MOD % MOD


for _ in range(int(input())):
    (n, k) = map(int, input().split())
    prod = 1
    l = [int(i) for i in input().split()]
    l.sort()
    for i in range(n):
        tot = nck(n - 1, k - 1)
        x = n - i
        asmin = nck(x - 1, k - 1)
        y = i + 1
        asmax = nck(y - 1, k - 1)
        req = tot - asmin - asmax
        prod = prod * pow(l[i], req, MOD) % MOD
    print(prod % MOD)
