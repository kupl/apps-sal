from bisect import *


def pair(fc, tc):
    bf = []
    maxb = 0
    ans = 0
    for f in fc:
        (p, b) = f
        maxpp = tc - p
        ii = bisect_left(bf, (maxpp + 1, 0)) - 1
        if ii >= 0:
            (pp, bb) = bf[ii]
            ans = max(ans, bb + b)
        if b > maxb:
            bf.append(f)
            maxb = b
    return ans


(n, c, d) = map(int, input().split())
arr1 = []
arr2 = []
for i in range(n):
    (b, k, t) = input().split()
    (b, k) = (int(b), int(k))
    if t == 'C' and k <= c:
        arr1.append((k, b))
    if t == 'D' and k <= d:
        arr2.append((k, b))
if len(arr1) > 0 and len(arr2) > 0:
    v1 = max(arr1, key=lambda x: x[1])[1] + max(arr2, key=lambda x: x[1])[1]
else:
    v1 = 0
v2 = pair(sorted(arr1), c)
v3 = pair(sorted(arr2), d)
print(max([v1, v2, v3]))
