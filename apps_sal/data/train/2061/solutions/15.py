import sys
from collections import defaultdict, Counter, namedtuple, deque
import itertools
import functools
import bisect
import heapq
import math
import copy


MOD = 10 ** 9 + 7

T = int(input())
for t in range(T):
    A = list(map(int, input().split()))
    mc = []
    for i in [0, 2, 4]:
        x, y = A[i], A[i + 1]
        c = 0
        if y == x:
            c = 2 * x - 1 if x > 0 else 2 * (-x)
        elif y == -x + 1:
            c = 2 * x - 2 if x > 0 else 2 * (-x)
        elif y > x:
            if y > -x + 1:
                c = 2 * y - 2
            else:
                c = 2 * (-x) - 1
        elif y < x:
            if y > -x + 1:
                c = 2 * x - 2
            else:
                c = 2 * (-y) - 1

        mc.append(c)

    vmax = max(mc)
    if vmax == 0:
        print((0))
    elif vmax == 1 and mc.count(0) == 2:
        print((1))
    elif mc.count(vmax) == 3:
        print((vmax + 2))
    elif mc.count(vmax) == 2:
        print((vmax + 1))
    elif mc.count(vmax - 1) == 2:
        print((vmax + 1))
    else:
        print(vmax)
