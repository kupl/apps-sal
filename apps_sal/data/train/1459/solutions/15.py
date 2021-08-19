import math
(n, m) = map(int, input().split())
hyp = math.sqrt(1 + m * m)
cosx = 1 / hyp
sinx = m / hyp
ptsx = []
ptsy = []
for i in range(n):
    (px, py) = list(map(int, input().strip().split()))
    ptsx.append(cosx * px + sinx * py)
    ptsy.append(cosx * py - sinx * px)
w = max(ptsx) - min(ptsx)
l = max(ptsy) - min(ptsy)
print(2 * l + 2 * w)
