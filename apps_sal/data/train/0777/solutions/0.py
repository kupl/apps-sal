import math
t = eval(input())
while t:
    t = t - 1
    (r1, h1, r2, h2) = list(map(float, input().split()))
    vol1 = math.pi * r1 * r1 * h1 / 3 + 2 * math.pi * r1 * r1 * r1 / 3
    vol2 = math.pi * r2 * r2 * h2
    print('%.8f %.8f' % (vol1, vol2))
