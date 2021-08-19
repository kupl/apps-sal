import math
for _ in range(0, int(input())):
    points = int(input())
    xs = set()
    ys = set()
    for _ in range(points):
        (x, y) = [int(i) for i in input().split()]
        xs.add(x - y)
        ys.add(x + y)
    xmin = 1000000001
    ymin = 1000000001
    if len(xs) != points or len(ys) != points:
        print(0)
    else:
        xs = sorted(xs)
        ys = sorted(ys)
        xmin = math.fabs(xs[1] - xs[0])
        ymin = math.fabs(ys[1] - ys[0])
        for i in range(1, len(xs) - 1):
            if xmin > math.fabs(xs[i + 1] - xs[i]):
                xmin = xs[i + 1] - xs[i]
            if ymin > math.fabs(ys[i + 1] - ys[i]):
                ymin = ys[i + 1] - ys[i]
        print(min(xmin, ymin) / 2)
