for i in range(int(input())):
    (s, sg, fg, d, t) = map(int, input().split())
    sc = s + d * 180 / t
    if abs(sg - sc) == abs(fg - sc):
        print('DRAW')
    elif abs(sg - sc) < abs(fg - sc):
        print('SEBI')
    elif abs(sg - sc) > abs(fg - sc):
        print('FATHER')
