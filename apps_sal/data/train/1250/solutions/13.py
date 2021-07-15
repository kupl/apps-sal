MOD = int(1e9 + 7)
for _ in range(int(input())):
    n = int(input()) + 1
    res = (((3*pow(3, n, MOD) - 3) % MOD) * 500000004)% MOD
    res = (res - (2*(pow(2, n, MOD) - 1)) % MOD) % MOD
    print(res)
