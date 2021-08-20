def solve1():
    maxx = maxy = 0
    minx = miny = 1000111000
    for i in range(n):
        maxx = max(maxx, x[i])
        minx = min(minx, x[i])
        maxy = max(maxy, y[i])
        miny = min(miny, y[i])
    return (maxx - minx) * (maxy - miny)


def solve2a(minx):
    miny = min(x)
    maxy = max(y)
    maxx = 0
    for i in range(n):
        if y[i] < minx:
            return 2 ** 60
        if minx <= x[i]:
            maxx = max(maxx, x[i])
        else:
            maxx = max(maxx, y[i])
    return (maxx - minx) * (maxy - miny)


def solve2_():
    res = 2 ** 60
    for minx in x:
        res = min(res, solve2a(minx))
    for minx in y:
        res = min(res, solve2a(minx))
    return res


def solve2():
    res = 2 ** 60
    xy = x + y
    xy.sort()
    miny = min(x)
    maxy = max(y)
    my = min(y)
    mx = max(x)
    pi = 0
    for minx in xy:
        if my < minx:
            break
        while pi < n and p[pi][0] < minx:
            pi += 1
        maxx = max(ly[pi], mx)
        res = min(res, (maxx - minx) * (maxy - miny))
    return res


n = int(input())
x = [0] * n
y = [0] * n
p = [(0, 0)] * n
mini = maxi = 0
for i in range(n):
    (x[i], y[i]) = list(map(int, input().split()))
    (x[i], y[i]) = (min(x[i], y[i]), max(x[i], y[i]))
    p[i] = (x[i], y[i])
    if x[i] < x[mini]:
        mini = i
    if y[maxi] < y[i]:
        maxi = i
p.sort()
ly = [0] * (n + 2)
my = 0
for i in range(n):
    my = max(my, p[i][1])
    ly[i + 1] = my
ans = solve1()
if mini != maxi:
    ans = min(ans, solve2())
print(ans)
