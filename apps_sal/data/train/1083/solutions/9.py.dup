for _ in range(int(input())):
    n, m, z, l, r, b = list(map(int, input().split()))
    r = r + l
    if m == 1:
        print(min(n * m, z + r + b))
    elif m % 2:
        p = r / (m - 1)
        k = min(b - p, (m + 1 - (r - p * (m - 1))) / 2 + ((n - p - 1) * ((m + 1) / 2))) + p
        print(min(n * m, z + r + k))
    else:
        p = r / (m - 1)
        k = min(b - p, (n - p) * (m / 2)) + p
        print(min(n * m, z + r + k))
