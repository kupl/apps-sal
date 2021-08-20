for t in range(int(input())):
    (x1, x2, x3, v1, v2) = [int(x) for x in input().rstrip().split()]
    t1 = abs(x3 - x1) / v1
    t2 = abs(x3 - x2) / v2
    if t1 < t2:
        print('Chef')
    elif t1 > t2:
        print('Kefa')
    elif t1 == t2:
        print('Draw')
    else:
        pass
