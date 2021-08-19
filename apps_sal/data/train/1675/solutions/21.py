import math


def calculate(a, b):
    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


t = int(input())
for _ in range(t):
    s = input()
    n = int(input())
    xcoord = []
    ycoord = []
    arr = []
    for i in range(n):
        (x, y) = map(int, input().strip().split())
        xcoord.append(x)
        ycoord.append(y)
    dist = 0
    arr = list(zip(xcoord, ycoord))
    arr.sort(key=lambda a: (a[0], a[1] * -1))
    for i in range(1, n):
        dist += calculate(arr[i - 1], arr[i])
    print('{:0.2f}'.format(dist))
