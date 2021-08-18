import math as m
tst, N = list(map(int, input().split()))
for i in range(tst):
    val = int(input())
    z = m.sqrt(val)
    s = m.floor(z)
    S = pow(s, 2)
    p = val - S
    q = (N * val) * (.01)
    if p <= q:
        print("yes")
    else:
        print("no")
