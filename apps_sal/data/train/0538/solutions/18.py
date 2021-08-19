for _ in range(int(input())):
    (s, sg, fg, d, t) = map(int, input().split())
    dif = float(d * 180 / t)
    diff = float(s) + dif
    if abs(float(diff - sg)) > abs(float(diff - fg)):
        print('FATHER')
    elif abs(float(diff - sg)) < abs(float(diff - fg)):
        print('SEBI')
    else:
        print('DRAW')
