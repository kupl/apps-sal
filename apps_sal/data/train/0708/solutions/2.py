for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    mod = 1000000007
    s = 0
    for i in range(1, n + 1):
        p = pow(k, (2 * i) - 1, mod)
        s = (s + p) % mod
        k = (p * k) % mod
    print(s)
