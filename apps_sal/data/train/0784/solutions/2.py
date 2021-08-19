import sys
import os
import random
import math
# nonlocal defs
n, m, p = list(map(int, input().split()))
a = [dict() for _ in range(n)]
for _ in range(p):
    i, j = list(map(int, input().split()))
    i -= 1
    j -= 1
    if j not in a[i]:
        a[i][j] = j + 1
    else:
        a[i][j] += 1


def chefbm(a, i):
    for (k, v) in a[i].items():
        if k == m - 1:
            continue
        if k + 1 in a[i]:
            c = a[i][k + 1]
        else:
            c = k + 1
        if a[i][k] > c:
            return -1
    y = a[i][m - 1] if m - 1 in a[i] else m - 1
    x = a[i][0] if 0 in a[i] else 0
    return y - x


for i in range(n):
    print(chefbm(a, i))
