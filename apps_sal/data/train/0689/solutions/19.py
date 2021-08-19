from collections import deque, defaultdict
from math import sqrt, ceil
import sys
import copy


def get_array():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))


def input():
    return sys.stdin.readline().strip()


n = int(input())
d = dict()
flag = 0
for i in range(n):
    (x, y) = get_ints()
    d[x] = y
for x in list(d.keys()):
    res = x + d[x]
    if res in list(d.keys()):
        if res + d[res] == x:
            flag = 1
            break
if flag == 1:
    print('YES')
else:
    print('NO')
