from functools import reduce
from operator import *
from math import *
from sys import *
from string import *
from collections import *
setrecursionlimit(10**7)
dX = [-1, 1, 0, 0, -1, 1, -1, 1]
dY = [0, 0, -1, 1, 1, -1, -1, 1]
def RI(): return list(map(int, input().split()))
def RS(): return input().rstrip().split()


n = RI()[0]
ti = [0] * 3
tot = [0] * 3
for i in range(n):
    t, x, y = RI()
    tot[t] += x
    ti[t] += 1
for i in (1, 2):
    print(["LIVE", "DEAD"][ti[i] * 5 > tot[i]])
