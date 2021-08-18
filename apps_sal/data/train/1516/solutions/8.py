MOD = 10**9 + 7
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = k
    b = n + k - 1
    c = (a - 1) % MOD
    req = a * 2 - b - 1
    d = n - 1
    if req > 0:
        if req % d == 0:
            nt = req // d
        else:
            nt = req // d + 1
        c += (((nt * (2 * req + (nt - 1) * (-d))) // 2) % MOD) % MOD
    print(c % MOD)
