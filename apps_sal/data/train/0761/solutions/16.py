import operator
from collections import Counter
from bisect import bisect_left

for _ in range(0, int(input())):
    [a, b, c] = list(map(int, input().strip().split()))
    x1 = list(map(int, input().strip().split()))
    x2 = list(map(int, input().strip().split()))
    y1 = list(map(int, input().strip().split()))
    z1 = list(map(int, input().strip().split()))
    x = list(map(operator.sub, x1, x2))
    x.sort()
    z = y1 + z1
    zc = Counter(z)
    z = list(zc.keys())
    z.sort()
    s = len(z)
    d = b + c
    tot = 0
    refpos = 0
    for p in x:
        pos = bisect_left(z, p) - 1
        if pos > -1:
            tot += p - z[pos]
            zc[z[pos]] -= 1
            d -= 1
            if zc[z[pos]] == 0:
                del z[pos]
                s -= 1
        else:
            tot += p
    print(tot)
