from collections import defaultdict
import sys
input = sys.stdin.readline


def inside(n, m, x, y):
    return 0 <= x <= n and 0 <= y <= m


def corner(n, m, x, y):
    return x in [0, n] and y in [0, m]


def next(n, m, x, y, t, a, b):
    for cx in [0, n]:
        cy = a * cx + b
        if inside(n, m, cx, cy) and (cx, cy) != (x, y):
            nx, ny = cx, cy
    for cy in [0, m]:
        cx = (cy - b) // a
        if inside(n, m, cx, cy) and (cx, cy) != (x, y):
            nx, ny = cx, cy
    nt = t + abs(nx - x)
    na = -a
    nb = ny - na * nx
    if corner(n, m, nx, ny):
        return None
    return nx, ny, nt, na, nb


n, m, k = list(map(int, input().split()))
d = defaultdict(list)
for i in range(k):
    x, y = list(map(int, input().split()))
    for a in [-1, 1]:
        b = y - a * x
        d[(a, b)].append((x, y, i))
ans = [-1] * k
ray = (0, 0, 0, 1, 0)
visit = set()
while ray:
    x, y, t, a, b = ray
    if (a, b) in visit:
        break
    visit.add((a, b))
    for sensor in d[(a, b)]:
        sx, sy, i = sensor
        if ans[i] == -1:
            ans[i] = t + abs(x - sx)
    ray = next(n, m, x, y, t, a, b)

for x in ans:
    print(x)
