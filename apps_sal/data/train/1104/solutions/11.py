t = int(input())

for _ in range(0, t):
    n, k = map(int, input().split())
    if n != 0:
        fn = n + (k // 2)
        if k % 2 == 0:
            print((fn**2 - fn + n) % 1000000007)
        else:
            print((fn**2 + fn - n) % 1000000007)
    else:
        print((k * (k - 1)) % 1000000007)
