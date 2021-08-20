import math
import os
import sys
from atexit import register
from io import StringIO
sys.stdout = StringIO()
register(lambda: os.write(1, sys.stdout.getvalue().encode()))
(n, m) = [int(k) for k in input().split()]
t = [0] * (4 * n)


def update(x, l, r, v, tl, tr):
    if r < l:
        return
    if t[v] != 0:
        return
    if l == tl and r == tr:
        t[v] = x
    else:
        tm = tl + tr >> 1
        update(x, l, min(tm, r), 2 * v, tl, tm)
        update(x, max(tm + 1, l), r, 2 * v + 1, tm + 1, tr)


def query(i):
    v = 1
    tl = 1
    tr = n
    while tl != tr:
        tm = tl + tr >> 1
        if i <= tm:
            v = v << 1
            tr = tm
        else:
            v = (v << 1) + 1
            tl = tm + 1
    k = 0
    while v != 0:
        k = k or t[v]
        v = v >> 1
    return k


for _ in range(m):
    (l, r, x) = [int(k) for k in input().split()]
    update(x, l, x - 1, 1, 1, n)
    update(x, x + 1, r, 1, 1, n)
print(' '.join([str(query(k)) for k in range(1, n + 1)]))
