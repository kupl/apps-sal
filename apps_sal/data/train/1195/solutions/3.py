for t in range(int(input())):
    (n, a, b, c, d, p, q, y) = map(int, input().split())
    x = list(map(int, input().split()))
    bf = abs(x[a - 1] - x[b - 1]) * p
    bt = abs(x[a - 1] - x[c - 1]) * p
    if bt <= y:
        wbt = y + abs(x[d - 1] - x[b - 1]) * p + abs(x[d - 1] - x[c - 1]) * q
        print(min(bf, wbt))
    else:
        print(bf)
