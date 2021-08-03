from itertools import chain
from functools import reduce
from operator import and_


def R(): return list(map(int, input().split()))


t = int(input())
for _ in range(t):
    n, *z = R()
    a = list(R())
    def aa(): return chain.from_iterable((x, -x) for x in a)
    r = 0
    v = [x + y for x in z for y in aa()]
    if 0 in v:
        print(1)
    elif 0 in reduce(and_, (set(x + y for x in v) for y in aa())):
        print(2)
    else:
        print(0)
