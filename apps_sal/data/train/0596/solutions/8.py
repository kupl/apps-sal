"""input
6
0 1
1 1
2 1
1 3
4 6
4 100
"""
from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict as dd
mod = 10 ** 9 + 7
for _ in range(int(input())):
    (n, k) = list(map(int, input().strip().split()))
    if k == 1:
        sm = pow(n, 2, mod)
        print(sm)
        continue
    elif n == 0:
        sm = k * (k - 1)
        print(sm % mod)
        continue
    else:
        sm = n * (n + 1) % mod
    y = (k - 1) / 2
    q = y
    if int(y) == y:
        y = max(0, int(y) - 1)
        rem = 2
    else:
        y = int(y)
        rem = 1
    sm += 2 * y * n % mod + y * (y + 1) % mod
    if rem == 1:
        sm += n
    else:
        sm += 2 * (n + y + 1) - n
    print(sm % mod)
