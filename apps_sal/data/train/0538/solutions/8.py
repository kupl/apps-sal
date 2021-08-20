for i in range(int(input())):
    (s, sg, fg, d, t) = list(map(int, input().split()))
    speed = d * 180 / t + s
    sa = abs(sg - speed)
    fa = abs(fg - speed)
    if fa < sa:
        print('FATHER')
    elif fa > sa:
        print('SEBI')
    else:
        print('DRAW')
