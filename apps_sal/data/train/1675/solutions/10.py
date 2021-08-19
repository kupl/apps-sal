from math import sqrt


def fun(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


for i in range(int(input())):
    input()
    n = int(input())
    a = []
    for i in range(n):
        (k, v) = map(int, input().split())
        a.append([k, v])
    a.sort(key=lambda x: [x[0], -x[1]])
    dis = 0
    for i in range(n - 1):
        dis += fun(a[i], a[i + 1])
    print('{0:.2f}'.format(dis))
