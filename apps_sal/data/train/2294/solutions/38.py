import sys
read = sys.stdin.read
readline = sys.stdin.readline

n, = list(map(int, readline().split()))

xy = []
for _ in range(n):
    x, y = list(map(int, readline().split()))
    if x > y:
        x, y = y, x
    xy.append((x, y))
xy.sort()


xx = []
yy = []
for x, y in xy:
    xx.append(x)
    yy.append(y)


ymaxr = yy[:]
for i in range(n - 2, -1, -1):
    ymaxr[i] = max(ymaxr[i], ymaxr[i + 1])

ymaxl = yy[:]
for i in range(1, n):
    ymaxl[i] = max(ymaxl[i], ymaxl[i - 1])

ymin = yy[:]
for i in range(1, n):
    ymin[i] = min(ymin[i], ymin[i - 1])


ans = 1 << 60
for i in range(n):
    mr = xx[0]

    Mr = xx[i]
    if i != n - 1:
        Mr = max(Mr, ymaxr[i + 1])

    mb = ymin[i]
    if i != n - 1:
        mb = min(mb, xx[i + 1])

    Mb = ymaxl[i]
    if i != n - 1:
        Mb = max(Mb, xx[n - 1])

    ans = min(ans, (Mr - mr) * (Mb - mb))


print(ans)
