t = int(input())
while t:
    li = [int(i) for i in input().split()]
    x1 = li[0]
    y1 = li[1]
    x2 = li[2]
    y2 = li[3]
    d1 = pow(pow(x1, 2) + pow(y1, 2), 0.5)
    d2 = pow(pow(x2, 2) + pow(y2, 2), 0.5)
    if d1 < d2:
        print('A IS CLOSER')
    else:
        print('B IS CLOSER')
    t -= 1
