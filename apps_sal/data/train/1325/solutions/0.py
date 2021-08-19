for j in range(int(input())):
    (p, q, r, s) = map(int, input().split())
    x = s - p
    y = s - q
    z = s - r
    print(y, z, x)
