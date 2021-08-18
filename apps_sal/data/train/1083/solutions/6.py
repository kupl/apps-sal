for _ in range(int(input())):
    n, m, z, l, r, b = list(map(int, input().split()))
    r = r + l
    if (m == 1):
        print(min(n * m, z + r + b))
        continue
    p = r / (m - 1)
    if (n <= p):
        print(min(n * m, z + r + b))
    else:
        s = min(b - p, (m + 1 - (r - p * (m - 1))) / 2 + ((n - p - 1) * ((m + 1) / 2))) + p
        R = r % (m - 1)
        h = R % (n - p)
        y = R / (n - p)
        k = min(b - p, ((m - y) / 2) * h + ((m + 1 - y) / 2) * (n - p - h)) + p
        print(max(min(n * m, z + r + s), min(n * m, z + r + k)))
