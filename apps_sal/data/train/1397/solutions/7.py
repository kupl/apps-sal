from collections import defaultdict
from bisect import bisect_right

I = input
t = int(I())
for _ in range(t):
  I()
  d = defaultdict(list)
  for i, x in enumerate(map(int, I().split())):
    d[x].append(i)
  i, m = -1, 1
  for x in sorted(d):
    l = d[x]
    j = bisect_right(l, i)
    i = l[j % len(l)]
    m += j // len(l)
  print(m)

