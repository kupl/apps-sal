import sys
import queue

t = int(input())


while(t):

    n = int(input())
    d = {}

    for i in range(n):
        line = input().split()
        x = int(line[0])
        y = int(line[1])
        if (x not in d):
            d[x] = y
        else:
            d[x] = max(d[x], y)

    p = list(d.items())

    n = len(p)
    for i in range(n):
        p[i] = (p[i][1], p[i][0])

    p.sort()
    # print(p)

    if (len(p) > 2):
        n = len(p)
        sys.stdout.write(str(p[n - 1][0] + p[n - 2][0] + p[n - 3][0]) + "\n")
    else:
        sys.stdout.write("0\n")

    t -= 1
