import fractions
for t in range(int(input())):
    (h, u, d) = list(map(int, input().split()))
    g = fractions.gcd(u, d)
    if h % g != 0:
        print(-1)
    else:
        m = 0
        n = -1
        while True:
            n = (float(m) * u - h) / d
            if n > 0 and int(n) == n:
                break
            m += 1
        print(int(m + n))
