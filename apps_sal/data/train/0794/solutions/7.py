from collections import defaultdict
m = pow(10, 9) + 7


def inv(i):
    return pow(i, m - 2, m)


def ifacto(n):
    if(n > len(ifact) - 1):
        for i in range(len(ifact), n + 1):
            temp = (inv(i) * ifact[i - 1]) % m
            ifact.append(temp)
    return ifact[n]


def facto(n):
    if(n > len(fact) - 1):
        for i in range(len(fact), n + 1):
            temp = (i * fact[i - 1]) % m
            fact.append(temp)
    return fact[n]


fact = [1]
ifact = [1]
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    d[0] = 1
    ans = 1
    ex = 0
    for i in a:
        d[i] = d[i] + 1
    for i in range(1, max(a) + 1):
        ans = (ans * pow(d[i - 1], d[i], m)) % m
        ex = ex + int((d[i] * (d[i] - 1)) / 2)
    if(k > n - 1):
        t = k - (n - 1)
        if(t > ex):
            ans = 0
        else:
            ans = ((ans * facto(ex)) % m * (ifacto(t) * ifacto(ex - t)) % m) % m
    print(ans)
