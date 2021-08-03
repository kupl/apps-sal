import sys

sys.setrecursionlimit(500005)
stdin = sys.stdin


def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))
def ns(): return stdin.readline().strip()


h, w, m = na()
rs = [0] * h
cs = [0] * w

se = set()
for i in range(m):
    r, c = na()
    rs[r - 1] += 1
    cs[c - 1] += 1
    se.add((r - 1) * w + c - 1)

rmax = max(rs)
cmax = max(cs)

remax = rs.count(rmax)
cemax = cs.count(cmax)
if remax * cemax > m:
    print(rmax + cmax)
    return

rmaxs = [i for i, _ in enumerate(rs) if _ == rmax]
cmaxs = [i for i, _ in enumerate(cs) if _ == cmax]
for r in rmaxs:
    for c in cmaxs:
        if r * w + c not in se:
            print(rmax + cmax)
            return
print(rmax + cmax - 1)
