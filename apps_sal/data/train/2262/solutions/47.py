(r, c, n) = list(map(int, input().split()))
points = []
xx = [0, r]
yy = [0, c]


def add(x, y):
    if x == 0:
        points.append(r * 2 + c + c - y)
    elif x == r:
        points.append(r + y)
    elif y == 0:
        points.append(x)
    else:
        points.append(r + c + r - x)


for i in range(n):
    (x0, y0, x1, y1) = list(map(int, input().split()))
    if (x0 in xx or y0 in yy) and (x1 in xx or y1 in yy):
        add(x0, y0)
        add(x1, y1)
index = list(range(len(points)))
index.sort(key=lambda a: points[a])
que = []
flag = True
for i in index:
    if que and que[-1] // 2 == i // 2:
        que.pop()
    else:
        que.append(i)
if que:
    print('NO')
else:
    print('YES')
