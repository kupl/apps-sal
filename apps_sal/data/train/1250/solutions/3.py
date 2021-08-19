tc = int(input())
while tc > 0:
    tc -= 1
    mod_inv = 500000004
    mod = 1000000007
    n = int(input())
    res = 4500000036 * (pow(3, n, mod) - 1) % mod - 4 * (pow(2, n, mod) - 1)
    print((res + 1) % mod)
