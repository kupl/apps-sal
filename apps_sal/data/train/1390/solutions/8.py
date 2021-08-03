import math
t = int(input())
for t1 in range(0, t):
    n, q = list(map(int, input().split()))

    ok = (q + n + 1) * q / (q + 1)
    print("{0:.6f}".format(ok))
