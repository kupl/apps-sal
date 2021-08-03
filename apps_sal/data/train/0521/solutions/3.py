from math import asin
import math


def ar(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt((s * (s - a) * (s - b) * (s - c)))


def dist(x1, y1, x2, y2):
    return math.sqrt((y2 - y1)**2 + (x2 - x1)**2)


def return_angle(a, b, c):
    return math.acos((a**2 + b**2 - c**2) / (2 * a * b))


t = int(input())
for _ in range(t):
    n = int(input())
    it = list(map(int, input().split()))
    x, y = map(int, input().split())
    it.sort()
    tot = 0
    vis = [0] * n
    pp = []
    for i in range(n):
        for j in range(i + 1, n):
            a = it[i]
            b = it[j]
            d = abs(a - b)
            d1 = dist(a, 0, x, y)
            d2 = dist(b, 0, x, y)
            ans = return_angle(d1, d2, d)
          #  r=(d1*d2*d)/(4*ar(d1,d2,d))
         #   ans=asin(d/(2*r))
            ans = abs(ans)
            pp.append([ans, i, j])
    pp.sort(reverse=True)
    for i in pp:
        if vis[i[1]] or vis[i[2]]:
            continue
        tot += i[0]
        vis[i[2]] = 1
        vis[i[1]] = 1
    print(tot)
