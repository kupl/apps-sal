for _ in range(int(input())):
    (n, m, z, l, r, b) = list(map(int, input().split()))
    r = r + l
    if m == 1:
        print(min(n * m, z + r + b))
        continue
    p = r / (m - 1)
    if m % 2 == 0 and r - p * (m - 1) <= n - p:
        k = min(b - p, (n - p) * (m / 2)) + p
        print(min(n * m, z + r + k))
    else:
        k = min(b - p, (m + 1 - (r - p * (m - 1))) / 2 + (n - p - 1) * ((m + 1) / 2)) + p
        print(min(n * m, z + r + k))
