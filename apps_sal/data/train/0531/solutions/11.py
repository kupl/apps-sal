from math import inf as inf
from math import *
from collections import *
import sys
from itertools import permutations
# input=sys.stdin.readline
n = int(input())
r = []
for i in range(n):
    a, h = list(map(int, input().split()))
    r.append([a, h])
s = 2
if(n == 1):
    print(1)
    return
prev = -10000000000000
for i in range(1, n - 1):
    prev = max(r[i - 1][0], prev)
    nex = r[i + 1][0]
    if(r[i][0] - r[i][1] > prev):
        s += 1
    elif(r[i][0] + r[i][1] < nex):
        s += 1
        prev = r[i][0] + r[i][1]
print(s)
