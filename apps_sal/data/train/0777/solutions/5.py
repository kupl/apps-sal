import math
t = int(input())
for i in range(t):
    (r1, h1, r2, h2) = [float(x) for x in input().split()]
    pi = math.pi
    temp1 = r1 ** 2 * pi * (h1 + 2 * r1) / 3
    temp2 = pi * r2 ** 2 * h2
    print('%.8f' % temp1, '%.8f' % temp2)
