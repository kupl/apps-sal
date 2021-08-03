for _ in range(int(input())):
    n, m, z, l, r, b = list(map(int, input().split()))
    r = r + l
    c = 0
    if m == 1:
        print(min(n * m, z + r + b))
        continue
    elif m % 2 == 0:
        m -= 1
        if n >= r:
            c += r
            R = n - r
            r = 0
            if z <= R:
                c += z
                z = 0
            else:
                c += R
                z -= R
        else:
            c += n
            r -= n
    b += (r % 2)
    r -= (r % 2)
    if m == 1:
        print(min(n * m, z + r + b) + c)
        continue
    p = r / (m - 1)
    k = min(b - p, (m + 1 - (r - p * (m - 1))) / 2 + (n - p - 1) * ((m + 1) / 2)) + p
    print(min(n * m, z + r + k) + c)
