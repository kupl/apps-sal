t = int(input())


def do():
    (x1, x2, x3, v1, v2) = list(map(int, input().split()))
    t1 = 0
    t2 = 0
    t1 = abs(x1 - x3) / v1
    t2 = abs(x2 - x3) / v2
    if t1 > t2:
        print('Kefa')
    elif t1 < t2:
        print('Chef')
    elif t1 == t2:
        print('Draw')
    else:
        pass
    return


for i in range(t):
    do()
