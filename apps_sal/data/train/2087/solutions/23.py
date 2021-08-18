""" My template """


import math
import itertools
n, L, R, Ql, Qr = list(map(int, input().split()))
w = list(map(int, input().split()))
pw = list(itertools.accumulate(w))
ts = sum(w)
ans = math.inf
for i in range(n + 1):
    l = i
    r = n - i
    if l > 0:
        lsum = pw[i - 1]
    else:
        lsum = 0
    rsum = ts - lsum
    if l < r:
        ans = min(ans, L * lsum + rsum * R + max((r - l - 1) * Qr, 0))
    else:
        ans = min(ans, L * lsum + rsum * R + max((l - r - 1) * Ql, 0))
print(ans)
