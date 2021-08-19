import getpass
import sys
if getpass.getuser() != 'frohenk':
    filename = 'half'
else:
    sys.stdin = open('input.txt')
import math
import string
import re
import random
from decimal import Decimal, getcontext
from collections import deque
mod = 10 ** 9 + 7


def ria():
    return [int(i) for i in input().split()]


(n, q) = ria()
ar = ria()
mx = max(ar)
ar = deque(ar)
mxs = -1
ans = []
for i in range(n * 3):
    a = ar.popleft()
    b = ar.popleft()
    ans.append([a, b])
    if a == mx and mxs == -1:
        mxs = i
    if a > b:
        ar.appendleft(a)
        ar.append(b)
    else:
        ar.appendleft(b)
        ar.append(a)
for i in range(q):
    m = ria()[0]
    m -= 1
    if mxs >= m:
        print(ans[m][0], ans[m][1])
    else:
        print(ans[(m - mxs) % (n - 1) + mxs][0], ans[(m - mxs) % (n - 1) + mxs][1])
