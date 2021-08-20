import cmath
from math import ceil, floor, sqrt


def float_round(num, places=0, direction=floor):
    return direction(num * 10 ** places) / float(10 ** places)


t = int(input())
a = float(1)
for i in range(t):
    s = list(map(int, input().split()))
    b = float(pow(s[0], 2))
    c = float(4 * pow(s[1], 2))
    d = float(b ** 2 - 4 * a * c)
    if d == 0:
        sol1 = abs((b - cmath.sqrt(d)) / (2 * a))
        m = []
        m.append(float_round(sqrt(sol1), 6, round))
        m.append(float_round(sqrt(b - sol1), 6, round))
        m.append(float_round(sqrt(b), 6, round))
        m.sort()
        for p in range(2):
            print(m[p], end=' ')
        print(m[2])
    elif d > 0:
        sol1 = abs((b - cmath.sqrt(d)) / (2 * a))
        sol2 = abs((b + cmath.sqrt(d)) / (2 * a))
        m = []
        m.append(float_round(sqrt(sol1), 6, round))
        m.append(float_round(sqrt(sol2), 6, round))
        m.append(float_round(sqrt(b), 6, round))
        m.sort()
        for p in range(2):
            print(m[p], end=' ')
        print(m[2])
    else:
        print(-1)
