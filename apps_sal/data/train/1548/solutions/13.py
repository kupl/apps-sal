from itertools import accumulate, count
from operator import sub

f = lambda x: accumulate(list(map(sub, x, count())), min)

for s in [*open(0)][2::2]:
 a = *list(map(int, s.split())),
 n = len(a)
 b = f(a)
 c = reversed([*f(reversed(a))])
 print(*(min(x + i, y + n + ~i) for i, x, y in zip(count(), b, c)))

