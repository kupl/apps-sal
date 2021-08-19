for _ in range(int(input())):
    (n, d) = map(str, input().split())
    k = list(n)
    (dd, c, n) = (d, 0, len(n))
    for x in range(n):
        if int(k[n - x - 1]) > int(d):
            k.pop(n - x - 1)
            c += 1
        else:
            d = k[n - x - 1]
    print(''.join(k) + c * dd)
