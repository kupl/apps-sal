import math
pi = math.pi
for t in range(int(input())):
    r1, h1, r2, h2 = list(map(float, input().split()))
    v_1 = (pi * (r1**2) * h1) / 3
    v_2 = (2 * pi * (r1**3) / 3)
    v_3 = (pi * (r2**2) * h2)
    a = v_1 + v_2
    b = v_3
    print("%.7f" % a, "%.7f" % b)
