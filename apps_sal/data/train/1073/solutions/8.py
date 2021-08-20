t = int(input())
for _ in range(t):
    mod = 10 ** 9 + 7
    (n, m) = [int(c) for c in input().split(' ')]
    if n == 1:
        print(m % mod)
        continue
    (a, b) = (m * (m - 1), m)
    if n == 2:
        print((a + b) % mod)
    else:
        for p in range(3, n + 1):
            temp = a
            a = (a % mod + b % mod) % mod
            a = a * (m - 1) % mod
            b = temp
        print((a + b) % mod)
