import sys
input = sys.stdin.readline

q = int(input())

for testcases in range(q):
    n = int(input())
    ROBOT = [list(map(int, input().split())) for i in range(n)]

    XMAX = 10**5
    XMIN = -10**5
    YMAX = 10**5
    YMIN = -10**5

    for x, y, a, b, c, d in ROBOT:
        if a == 0:
            XMIN = max(XMIN, x)
        if b == 0:
            YMAX = min(YMAX, y)
        if c == 0:
            XMAX = min(XMAX, x)
        if d == 0:
            YMIN = max(YMIN, y)

    # print(XMIN,XMAX,YMIN,YMAX)

    if XMIN > XMAX or YMIN > YMAX:
        print(0)
    else:
        print(1, XMIN, YMIN)
