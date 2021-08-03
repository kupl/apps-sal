# cook your dish here
import math
root = math.sqrt(2)

for t in range(int(input())):
    num = int(input())

    a = []

    for i in range(num):
        a.append(list(map(int, input().split())))

    b = []
    c = []

    for i in range(num):
        b.append(a[i][1] - a[i][0])
        c.append(a[i][1] + a[i][0])

    c.sort(reverse=True)
    b.sort(reverse=True)

    d = []
    e = []

    for i in range(num - 1):
        d.append(b[i] - b[i + 1])
        e.append(c[i] - c[i + 1])

    f = min(min(d), min(e))

    f /= 2

    print(f)
