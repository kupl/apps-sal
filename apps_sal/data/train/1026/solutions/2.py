for _ in range(int(input())):
    a = [int(x) for x in input().split()]
    p = 1
    d = 0
    a.sort()
    mod = (10**9) + 7
    for v in a:
        p = (p * (v - d)) % mod
        d += 1
    print(p % mod)
