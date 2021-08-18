

z = int(input())
i = 0
while i < z:
    n = int(input())
    p = int(n**(0.5))
    if p * (p + 1) < n:
        p += 1
    x, y = 0, 0
    q = 0
    flag = True
    if p * (p + 1) == n:
        q = p
    else:
        q = p - 1
        flag = False
    if q % 2:
        x -= ((q + 1) // 2)
        y += ((q + 1) // 2)
    else:
        x += (q // 2)
        y -= (q // 2)
    if flag:
        print(x, y)
    else:
        l = q * (q + 1)
        t = p * (p + 1)
        diff = t - l

        if x < 0:
            if n - l >= diff // 2:
                y *= (-1)
                l += (diff // 2)
                x += (n - l)
            else:
                y -= (n - l)

        else:
            if n - l >= diff // 2:
                y *= (-1)
                y += 1
                l += (diff // 2)
                x -= (n - l)
            else:
                y += (n - l)
        print(x, y)
    i += 1
