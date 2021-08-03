from itertools import accumulate, count
from operator import add, sub


def f(x): return accumulate(list(map(sub, x, count())), min)


for s in [*open(0)][2::2]:
    a = *list(map(int, s.split())),
    n = len(a)
    b = f(a)
    c = reversed([*f(reversed(a))])
    print(*(list(map(min, list(map(add, b, count())), list(map(sub, c, count(1 - n)))))))
