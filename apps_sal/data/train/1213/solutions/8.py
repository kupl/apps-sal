for _ in range(int(input())):
    (x1, x2, x3, v1, v2) = map(int, input().split())
    d1 = abs(x3 - x1)
    d2 = abs(x2 - x3)
    t1 = d1 / v1
    t2 = d2 / v2
    if t1 > t2:
        print('Kefa')
    elif t1 < t2:
        print('Chef')
    else:
        print('Draw')
