import math


n, m = map(int, input().split())
pts = [list(map(int, input().strip().split())) for i in range(n)]

hyp = math.sqrt(1 + m * m)
cosx = 1 / hyp
sinx = m / hyp

pts = [[cosx * p[0] + sinx * p[1], -sinx * p[0] + cosx * p[1]] for p in pts]

w = max(pts, key=lambda x: x[0])[0] - min(pts, key=lambda x: x[0])[0]
l = max(pts, key=lambda x: x[1])[1] - min(pts, key=lambda x: x[1])[1]

print(2 * l + 2 * w)
