from collections import defaultdict
from bisect import bisect_right
I = input
t = int(I())
for _ in range(t):
    I()
    d = defaultdict(list)
    for (i, x) in enumerate(map(int, I().split())):
        d[x].append(i)
    (i, m) = (-1, 1)
    for x in sorted(d):
        l = d[x]
        j = bisect_right(l, i)
        if j == len(l):
            m += 1
            j = 0
        i = l[j]
    print(m)
