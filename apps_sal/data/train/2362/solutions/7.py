import sys

t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline())
    xMin, xMax, yMin, yMax = -100000, 100000, -100000, 100000
    x, y = 0, 0
    res = 1
    for i in range(n):
        xi, yi, xMinus, yPlus, xPlus, yMinus = list(map(int, sys.stdin.readline().split()))
        if xMinus == 0:
            xMin = max(xi, xMin)
        if xPlus == 0:
            xMax = min(xi, xMax)
        if yMinus == 0:
            yMin = max(yi, yMin)
        if yPlus == 0:
            yMax = min(yi, yMax)
    if xMin <= xMax and yMin <= yMax:
        print(1, xMin, yMin)
    else:
        print(0)
