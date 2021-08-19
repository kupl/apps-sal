import math
(n, m) = map(int, input().split())
hyp = math.sqrt(1 + m * m)
cosx = 1 / hyp
sinx = m / hyp
for i in range(n):
    p = list(map(int, input().strip().split()))
    px = cosx * p[0] + sinx * p[1]
    py = cosx * p[1] - sinx * p[0]
    if i == 0:
        left = px
        rght = px
        lowr = py
        uppr = py
    else:
        left = min(left, px)
        rght = max(rght, px)
        lowr = min(lowr, py)
        uppr = max(uppr, py)
w = rght - left
l = uppr - lowr
print(2 * l + 2 * w)
