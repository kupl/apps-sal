import math
pi = math.pi
# print pi
t = eval(input())
while(t != 0):
    a = list(map(float, input().split(' ')))
    vc = pi / 3 * (a[0] * a[0] * a[1] + 2 * a[0] * a[0] * a[0])
    vp = pi * a[2] * a[2] * a[3]
    print("%.10f %.10f" % (vc, vp))
    t = t - 1
