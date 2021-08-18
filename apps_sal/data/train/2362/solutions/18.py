import sys
inf = 10**5
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    a = []
    for i in range(n):
        a.append(list(map(int, sys.stdin.readline().split())))
    xl = -inf
    xh = 10**5
    yl = -inf
    yh = 10**5
    for i in range(n):
        if a[i][2] == 0:
            xl = max(xl, a[i][0])
        else:
            xl = max(xl, -inf)
        if a[i][3] == 0:
            yh = min(yh, a[i][1])
        else:
            yh = min(yh, 10**5)

        if a[i][4] == 0:
            xh = min(xh, a[i][0])
        else:
            xh = min(xh, 10**5)
        if a[i][5] == 0:
            yl = max(yl, a[i][1])
        else:
            yl = max(yl, -inf)

    if xl <= xh and yl <= yh:
        print(1, xl, yl)
    else:
        print(0)
