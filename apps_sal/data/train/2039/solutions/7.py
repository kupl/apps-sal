import heapq
import sys
import bisect
from collections import defaultdict

from itertools import product


n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))

l, r = -1, m


def check_v(v):
    M = 0
    for el in arr:
        if el <= M:
            if el + v >= M:
                continue
            else:
                return False
        else:
            if el + v >= M + m:
                continue
            else:
                M = el
    return True


while r - l > 1:
    mid = (l + r) // 2
    if check_v(mid):
        r = mid
    else:
        l = mid
print(r)
