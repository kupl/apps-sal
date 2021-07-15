from collections import defaultdict
from fractions import Fraction
from bisect import bisect_left as bisect

harmonic = [0] + [Fraction(sum({y for x in range(1,int(n**.5)+1) for y in [x, n//x] if not n%x}), n) for n in range(1,7001)]

harmonicity = defaultdict(set)
for n,h in enumerate(harmonic): harmonicity[h].add(n)

HARMO_GROUPS = {h: sorted(s) for h,s in harmonicity.items() if len(s) > 1}
HARMO_RATIOS = {n: h for h,lst in HARMO_GROUPS.items() for n in lst}
HARMO_NUM    = sorted(HARMO_RATIOS.keys())

def solve(a,b):
    seens, s = set(), 0
    n1, n2 = bisect(HARMO_NUM, a), bisect(HARMO_NUM, b)
    for n in HARMO_NUM[n1:n2]:
        if n not in seens:
            grp = [x for x in HARMO_GROUPS[HARMO_RATIOS[n]] if a <= x < b]
            if len(grp) > 1:
                seens |= set(grp)
                s += grp[0]
    return s
