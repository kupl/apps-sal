# -*- coding: utf-8 -*-
def input_str(row):
    res = []
    for _ in range(row):
        res.append(input().split())
    return res

N = int(input())
balls = input_str(N)
balls = sorted([sorted([int(x), int(y)]) for x, y in balls], key=lambda x: x[0])
#rmin == min, bmax == max
xmax = max(balls, key=lambda x: x[0])[0]
xmin = min(balls, key=lambda x: x[0])[0]
ymax = max(balls, key=lambda x: x[1])[1]
ymin = min(balls, key=lambda x: x[1])[1]
res1 = (xmax - xmin) * (ymax - ymin)

maxdiff = max(xmax, ymax) - min(xmin, ymin)
#rmin == min, rmax == max
diff = xmax - xmin
mina = xmax

for i in range(N)[:-1]:
    mina = min(balls[i][1], mina)
    xmax = max(balls[i][1], xmax)
    xmin = min(balls[i+1][0], mina)
    diff = min(diff, xmax - xmin)

res2 = maxdiff * diff

print(min(res1, res2))

