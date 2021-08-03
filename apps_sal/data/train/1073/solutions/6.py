mod = 10**9 + 7
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    if n == 1:
        print(m % mod)
        continue
    if n == 2:
        print((m % mod) * (m % mod) % mod)
        continue
    if m == 1:
        print(0)
        continue

    t = 0

    t1 = m % mod
    t2 = ((m % mod) * (m % mod) % mod)
    for i in range(3, n + 1):
        t = ((t1 + t2) % mod * (m - 1) % mod) % mod
        t1 = t2
        t2 = t
    print(t)
