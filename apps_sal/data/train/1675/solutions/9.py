from bisect import *
from collections import *
from sys import stdin, stdout
from queue import *
from itertools import *
from heapq import *
from random import *
from statistics import *
from math import *
import operator
inn = stdin.readline
out = stdout.write


def fun(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5


for i in range(int(input())):
    input()
    n = int(input())
    a = []
    for i in range(n):
        (k, v) = map(int, input().split())
        a.append((k, v))
    d = list(sorted(a, key=lambda x: [x[0], -x[1]]))
    dis = 0
    for i in range(n - 1):
        dis += fun(d[i], d[i + 1])
        t = d[i]
    print('%.2f' % dis)
