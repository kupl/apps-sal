import math


n, m = map(int, input().split())
pts = [list(map(int, input().strip().split())) for i in range(n)]

hyp = math.sqrt(1 + m * m)
cosx = 1 / hyp
sinx = m / hyp

for apt in pts:
    apt[0], apt[1] = (cosx * apt[0] + sinx * apt[1], -sinx * apt[0] + cosx * apt[1])

l = max(a[0] for a in pts) - min(a[0] for a in pts)
w = max(a[1] for a in pts) - min(a[1] for a in pts)

print(2 * l + 2 * w)
