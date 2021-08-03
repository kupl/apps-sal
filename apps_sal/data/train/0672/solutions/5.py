from math import sqrt


def distance():
    m = (y2 - y1) / (x2 - x1)
    dis = (q - m * p + m * x1 - y1) / sqrt(m * m + 1)
    return abs(dis)


for _ in range(int(input())):
    print("Test case :", _ + 1)
    x1, y1, x2, y2 = map(int, input().split())
    Q = int(input())
    for query in range(Q):
        p, q = map(int, input().split())
        if x1 == x2:
            if p == x1:
                print('YES')
            else:
                print('NO')
                print("{0:.6f}".format(abs(x1 - p)))
        elif x1 == p:
            print('NO')
            print("{0:.6f}".format(distance()))
        elif (y1 - y2) / (x1 - x2) == (y1 - q) / (x1 - p):
            print('YES')
        else:
            print('NO')
            print("{0:.6f}".format(distance()))
