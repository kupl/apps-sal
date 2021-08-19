for x in range(int(input())):
    (n, m) = map(int, input().split())
    y = n * m
    l = []
    for x in range(n * m):
        p = x + 1
        if y % p == 0:
            ans = 2 * (y // p)
        else:
            ans = 2 * (y // p + 1)
        mu = 0
        while mu < y:
            n1 = mu // m
            m1 = mu % m
            y2 = m1 * n + n1
            if y2 % (x + 1) == 0:
                ans -= 1
            mu += x + 1
        print(ans, end=' ')
    print('')
