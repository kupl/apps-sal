import sys
input = sys.stdin.readline
n = int(input())
xy = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    if xy[i][0] > xy[i][1]:
        xy[i][0], xy[i][1] = xy[i][1], xy[i][0]
if n == 1:
    print(0)
    return
x = list(zip(*xy))[0]
y = list(zip(*xy))[1]
xmax = max(x)
ymax = max(y)
xmin = min(x)
ymin = min(y)
ans = (xmax - xmin) * (ymax - ymin)
r = ymax - xmin
cand = []
for i in range(n):
    if xy[i] == [xmin, ymax]:
        print(ans)
        return
    if xy[i][0] == xmin:
        cand.append(xy[i][1])
    if xy[i][1] == ymax:
        cand.append(xy[i][0])
bmax = max(cand)
bmin = min(cand)
cons = []
for i in range(n):
    if xy[i][1] < bmin:
        bmin = xy[i][1]
    elif xy[i][0] > bmax:
        bmax = xy[i][0]
for i in range(n):
    if xy[i][0] < bmin and xy[i][1] > bmax:
        cons.append(xy[i])
if not cons:
    print(min(ans, r * (bmax - bmin)))
    return
cons.sort(key=lambda x: x[1])
lc = len(cons) + 1
cols = [[0 for i in range(2)] for j in range(lc)]
for i in range(lc)[::-1]:
    if i >= 1:
        cols[i][1] = cons[i - 1][1]
    else:
        cols[i][1] = bmax
    if i == lc - 1:
        cols[i][0] = bmin
    else:
        cols[i][0] = min(cols[i + 1][0], cons[i][0])
for i in range(lc):
    ans = min(ans, r * (cols[i][1] - cols[i][0]))
print(ans)
