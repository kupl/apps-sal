from bisect import *

n, tc, td = [int(i) for i in input().split()]
fc = []
fd = []
mbc = 0
mbd = 0
for _ in range(n):
    b, p, ft = input().split()
    b, p = int(b), int(p)
    f = (p, b)
    if ft == 'C':
        if p <= tc:
            fc.append(f)
            mbc = max(mbc, b)
    else:
        if p <= td:
            fd.append(f)
            mbd = max(mbd, b)

fc = sorted(fc)
fd = sorted(fd)


def pick2(fc, tc):
    bf = []
    maxb = 0
    ans = 0
    for f in fc:
        p, b = f
        maxpp = tc - p
        ii = bisect_left(bf, (maxpp + 1, 0)) - 1
        if ii >= 0:
            pp, bb = bf[ii]
            ans = max(ans, bb + b)
        if b > maxb:
            bf.append(f)
            maxb = b
    return ans


ans = mbc + mbd if mbc > 0 and mbd > 0 else 0
ans = max(ans, pick2(fc, tc))
ans = max(ans, pick2(fd, td))

print(ans)
