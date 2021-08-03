for _ in range(int(input())):
    n, a = list(map(int, input().split()))
    sum = 0
    mod = 10**9 + 7
    a1 = a
    for i in range(1, n + 1):
        p = 2 * i - 1
        a = pow(a, p, mod)
        sum = (sum + a % mod) % mod
        a = (a1 * a)
        a = a % mod
        a1 = a
    print(sum)
