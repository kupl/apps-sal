# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/1/14 22:22

"""


def solve(N, M, A):
    def check(ops):
        pv = 0
        for v in A:
            if v + ops < M:
                if v + ops < pv:
                    return False
                pv = max(pv, v)
            else:
                d = (v + ops) % M
                if d >= pv:
                    pass
                else:
                    pv = max(pv, v)
        return True

    lo, hi = 0, max(N, M)
    while lo <= hi:
        m = (lo + hi) // 2
        if check(m):
            hi = m - 1
        else:
            lo = m + 1
    return lo



N, M = map(int, input().split())
A = [int(x) for x in input().split()]
print(solve(N, M, A))
