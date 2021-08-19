t = int(input())
for i in range(t):
    (x1, x2, x3, v1, v2) = [int(x) for x in input().split()]
    d1 = x3 - x1
    d2 = x2 - x3
    if d1 / v1 < d2 / v2:
        print('Chef')
    elif d1 / v1 > d2 / v2:
        print('Kefa')
    else:
        print('Draw')
