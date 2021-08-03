for _ in range(int(input())):
    s, sg, fg, d, t = map(int, input().split())
    dis = (d * 50) / 1000
    t1 = t / 60
    speed = d * 50 * 60 * 60 / (t * 1000)
    speed += s
    if(abs(speed - sg) > abs(speed - fg)):
        print('FATHER')
    elif(abs(speed - sg) < abs(speed - fg)):
        print('SEBI')
    else:
        print('DRAW')
