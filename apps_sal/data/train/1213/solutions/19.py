t = int(input())
while t:
    (x_1, x_2, x_3, v_1, v_2) = list(map(int, input().split(' ')))
    t1 = abs(x_3 - x_1) / v_1
    t2 = abs(x_2 - x_3) / v_2
    if t1 < t2:
        print('Chef')
    elif t1 > t2:
        print('Kefa')
    else:
        print('Draw')
    t = t - 1
