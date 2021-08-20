import sys
import math
PI = math.pi
for __ in range(eval(input())):
    (r1, h1, r2, h2) = list(map(float, sys.stdin.readline().split()))
    print('%.6f %.6f' % (float(1) / float(3) * PI * r1 * r1 * h1 + float(2) / float(3) * PI * r1 * r1 * r1, PI * r2 * r2 * h2))
