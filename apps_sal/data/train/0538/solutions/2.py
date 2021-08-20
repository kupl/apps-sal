for i in range(int(input())):
    (s, sg, fg, d, t) = [int(i) for i in input().split()]
    dis = d * 50
    speed = dis / t
    exs = speed * 18 / 5
    ts = s + exs
    ss = abs(sg - ts)
    sf = abs(fg - ts)
    if ss > sf:
        print('FATHER')
    elif ss < sf:
        print('SEBI')
    elif ss == sf:
        print('DRAW')
