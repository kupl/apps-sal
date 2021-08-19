import math as m
(tst, N) = list(map(int, input().split()))
for i in range(tst):
    val = int(input())
    s = int(m.sqrt(val))
    S = pow(s, 2)
    p = val - S
    q = int(N * val * 0.01)
    if p <= q:
        print('yes')
    else:
        print('no')
