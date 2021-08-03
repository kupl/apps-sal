import sys
pi = 3.1415926535897
t = int(sys.stdin.readline())
for tc in range(t):
    r1, h1, r2, h2 = list(map(float, sys.stdin.readline().split()))
    v = pi * r1 * r1 * h1 / 3
    v += (pi * r1 * r1 * r1 * 4.0 / 3.0) / 2.0
    c = pi * r2 * r2 * h2
    print("%.9f" % v, "%.9f" % c)
