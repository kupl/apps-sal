def gcd(n1, n2):
    m = 1
    di = 2
    while di <= min(n1, n2) and (n1 > 1 and n2 > 1):
        if n1 % di == 0 and n2 % di == 0:
            n1 //= di
            n2 //= di
            m *= di
        else:
            di += 1
    return m


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    (mi, d) = (a[1] - a[0], [a[1] - a[0]])
    for i in range(2, n):
        d += [a[i] - a[i - 1]]
        if d[i - 1] % mi != 0:
            mi = gcd(mi, d[i - 1])
    d += [360 - a[n - 1] + a[0]]
    if d[n - 1] % mi != 0:
        mi = gcd(mi, d[n - 1])
    print(360 // mi - n)
