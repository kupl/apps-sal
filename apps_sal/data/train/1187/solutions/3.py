import sys
input = sys.stdin.readline
inp, ip = lambda: int(input()), lambda: [int(w) for w in input().split()]

M = 998244353
for _ in range(inp()):
    n, m = ip()
    size, ways = 0, 1
    a, b = 1, m
    for k in range(1, 70):
        if a > n:
            break
        ct = (n // a - n // b) - (n // a // m - n // b // m)
        size += ct * ((1 + k) // 2)
        if k % 2 == 0:
            ways = (ways * pow(k // 2 + 1, ct, M)) % M
        a, b = a * m, b * m
    print(size, ways)
