t = int(input())
i = 0
while i < t:
    n = int(input())
    c = 0
    z = 0
    if n >= 100:
        a = n // 100
        n = n - 100 * a
        z = a
    if n >= 50:
        b = n // 50
        n = n - 50 * b
        z = z + b
    if n >= 10:
        c = n // 10
        n = n - 10 * c
        z = z + c
    if n >= 5:
        d = n // 5
        n = n - 5 * d
        z = z + d
    if n >= 2:
        e = n // 2
        n = n - 2 * e
        z = z + e
    if n == 1:
        print(z + 1)
    else:
        print(z)
    i += 1
