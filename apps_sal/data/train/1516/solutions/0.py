__author__ = 'Prateek'
MOD = int(10 ** 9 + 7)


def test():
    (n, k) = list(map(int, input().split()))
    l = k
    d = n - 1
    ans = l - 1
    ans = ans % MOD
    a = k - n
    term = (d + a) // d
    ll = (a % MOD - (term - 1) % MOD * (d % MOD) % MOD) % MOD
    if ll < 0:
        ll = (ll + MOD) % MOD
    m = term % MOD * ((a % MOD + ll % MOD) % MOD) % MOD
    m = m * pow(2, MOD - 2, MOD) % MOD
    ans += m
    ans = ans % MOD
    print(ans)


if __author__ == 'Prateek':
    t = int(input())
    for _ in range(t):
        test()
