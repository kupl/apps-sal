import operator
import itertools
import bisect

def maxl(l, m, mx):
    l.sort(key=operator.itemgetter(1))
    lp = [p for(b, p) in l]
    lb = list(itertools.accumulate((b for (b, p) in l), max))
    for i, (b, p) in enumerate(l):
        k = bisect.bisect_right(lp, m - p, 0, i)
        if k:
            x = b + lb[k - 1]
            if x > mx:
                mx = x
    return mx

 
fc = []
fd = []

n, c, d = list(map(int, input().split()))
for _ in range(n):
    b, p, m = input().split()
    b, p = int(b), int(p)
    f, cd = (fc, c) if m == 'C' else (fd, d)
    if p <= cd:
        f.append((b, p))

mx = 0
if fc and fd:
    bc = max(b for (b, p) in fc)
    bd = max(b for (b, p) in fd)
    mx = bc + bd
mx = maxl(fc, c, mx)
mx = maxl(fd, d, mx)

print(mx)

