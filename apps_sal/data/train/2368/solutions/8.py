from decimal import Decimal
from fractions import Fraction
import sys
import math
import io
import os
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter


def data():
    return sys.stdin.readline().strip()


def mdata():
    return list(map(int, data().split()))


def outl(var):
    sys.stdout.write(' '.join(map(str, var)) + '\n')


def out(var):
    sys.stdout.write(str(var) + '\n')


INF = float('inf')
mod = int(1000000000.0) + 7
for t in range(int(data())):
    n = int(data())
    a = mdata()
    b = mdata()
    (a1, b1) = (min(a), min(b))
    ans = 0
    for i in range(n):
        ans += max(a[i] - a1, b[i] - b1)
    print(ans)
