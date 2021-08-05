for t in range(int(input())):
    n, k = map(int, input().split())
    mod = 10**9 + 7
    if n == 0:
        if k == 1:
            print(0)
        else:
            print(k * (k - 1) % mod)
    else:
        if k % 2 == 0:
            a = n + k // 2 - 1
            print((a * (a + 1) + n) % mod)
        else:
            a = n + k // 2
            print((a * (a + 1) - n) % mod)
