import numpy as np
n = int(input())
a = np.array(input().split(), dtype=np.int32)
b = np.array(input().split(), dtype=np.int32)


def f(t, a, b):
    power = 1 << t
    mask = (power << 1) - 1
    aa = a & mask
    bb = b & mask
    aa.sort()
    bb.sort()
    (x1, x2, x3) = (np.searchsorted(bb, v - aa).sum() for v in [power, power * 2, power * 3])
    zero_cnt = x1 + (x3 - x2)
    return (n - zero_cnt) % 2


ans = 0
for t in range(30):
    x = f(t, a, b)
    if x == 1:
        ans += 1 << t
print(ans)
