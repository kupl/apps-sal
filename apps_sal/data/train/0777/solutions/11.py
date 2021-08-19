from math import pi


def solve():
    s = input().split(' ')
    r1 = float(s[0])
    h1 = float(s[1])
    r2 = float(s[2])
    h2 = float(s[3])
    vCone = 1.0 / 3 * pi * r1 * r1 * h1 + 2.0 / 3 * pi * r1 * r1 * r1
    vCyl = pi * r2 * r2 * h2
    print('%0.6f %0.6f' % (vCone, vCyl))


t = int(input())
i = 0
while i < t:
    solve()
    i += 1
