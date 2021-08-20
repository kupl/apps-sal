for x in range(int(input())):
    (n, m) = map(int, input().split())
    y = n * m
    l = [(1, 1)]
    for x in range(n * m):
        l = [(1, 1)]
        a = 1
        b = 1
        while True:
            b = b + x + 1
            if b > m:
                u = b - m
                if u % m == 0:
                    a = a + u // m
                    b = m
                else:
                    a = a + u // m + 1
                    b = u % m
            if a > n:
                break
            else:
                l.append((a, b))
        a = 1
        b = 1
        while True:
            a = a + x + 1
            if a > n:
                u = a - n
                if u % n == 0:
                    b = b + u // n
                    a = n
                else:
                    b = b + u // n + 1
                    a = u % n
            if b > m:
                break
            else:
                l.append((a, b))
        print(len(set(l)), end=' ')
    print('')
