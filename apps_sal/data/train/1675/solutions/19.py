from math import sqrt


def dist(a, b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    return sqrt((x1 - x2)**2 + (y2 - y1)**2)


t = int(input())
for _ in range(t):
    blank = input()
    n = int(input())
    arr = []
    for j in range(n):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda a: (a[0], a[1] * -1))
    d = 0
    for i in range(len(arr) - 1):
        d += dist(arr[i], arr[i + 1])
    print("{:0.2f}".format(d))
