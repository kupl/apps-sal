import sys

t = int(sys.stdin.readline())
x = 'RGB'
y = 'GBR'
z = 'BRG'
for i in range(t):
    n, k = list(map(int, sys.stdin.readline().strip().split()))
    a = sys.stdin.readline().strip()
    xk = x
    yk = y
    zk = z

    op = 2001

    xd = []
    yd = []
    zd = []
    xdc = 0
    ydc = 0
    zdc = 0
    b = a
    for j in range(k):
        if(b[j] != xk[j % 3]):
            xd.append(1)
            xdc += 1
        else:
            xd.append(0)

        if(b[j] != yk[j % 3]):
            yd.append(1)
            ydc += 1
        else:
            yd.append(0)

        if(b[j] != zk[j % 3]):
            zdc += 1
            zd.append(1)
        else:
            zd.append(0)
    op = min(xdc, ydc, zdc)

    for j in range(k, n):
        if(b[j] != xk[j % 3]):
            xd.append(1)
            xdc += 1
        else:
            xd.append(0)

        if(b[j] != yk[j % 3]):
            yd.append(1)
            ydc += 1
        else:
            yd.append(0)

        if(b[j] != zk[j % 3]):
            zdc += 1
            zd.append(1)
        else:
            zd.append(0)
        xdc -= xd[j - k]
        ydc -= yd[j - k]
        zdc -= zd[j - k]
        op = min(op, xdc, ydc, zdc)
    print(op)
