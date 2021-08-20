from sys import *


def check(u, d, l, r):
    used = [pointsx[i][1] for i in range(l)]
    used += [pointsx[-1 - i][1] for i in range(r)]
    used += [pointsy[i][1] for i in range(u)]
    used += [pointsy[-1 - i][1] for i in range(d)]
    if len(set(used)) > k:
        return DOHERA
    dx = pointsx[-1 - r][0] - pointsx[l][0]
    dy = pointsy[-1 - d][0] - pointsy[u][0]
    dx += dx & 1
    dy += dy & 1
    dx = max(2, dx)
    dy = max(2, dy)
    return dx * dy


(n, k) = list(map(int, input().split()))
pointsx = []
pointsy = []
DOHERA = 10 ** 228
for i in range(n):
    a = list(map(int, input().split()))
    pointsx += [(a[0] + a[2], i)]
    pointsy += [(a[1] + a[3], i)]
(pointsx, pointsy) = (sorted(pointsx), sorted(pointsy))
ans = DOHERA
for u in range(0, k + 1):
    for d in range(0, k + 1):
        for l in range(0, k + 1):
            for r in range(0, k + 1):
                if l + r <= k and u + d <= k:
                    ans = min(ans, check(u, d, l, r))
print(ans // 4)
