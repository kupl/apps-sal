MOD = 10**9 + 7
p = 6000
fact = [0] * p
fact[0] = 1
for i in range(1, p):
    fact[i] = (fact[i - 1] * i) % MOD


def MI(a, MOD):
    return pow(a, MOD - 2, MOD)


def nck(n, k):
    if n == k or k == 0:
        return 1
    if n < k:
        return 0
    return fact[n] * MI(fact[k], MOD) * MI(fact[n - k], MOD) % MOD


for _ in range(int(input())):
    n, k = map(int, input().split())
    prod = 1
    l = [int(i) for i in input().split()]
    l.sort()
    # nck=combo_nck(n,k)
    for i in range(n):
        tot = nck(n - 1, k - 1)
        # print(tot)
        x = n - i
        if x >= k - 1:
            asmin = nck(x - 1, k - 1)
        else:
            asmin = 0
        y = i + 1
        if y >= k - 1:
            asmax = nck(y - 1, k - 1)
        else:
            asmax = 0
        # print(asmin)
        # print(asmin,asmax)
        prod *= pow(l[i], tot - asmin - asmax, MOD)
        # print(prod)
    print(prod % MOD)
