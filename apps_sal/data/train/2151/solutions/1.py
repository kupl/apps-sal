import collections
import atexit
import math
import sys
import bisect
sys.setrecursionlimit(1000000)


def getIntList():
    return list(map(int, input().split()))


try:
    import numpy

    def dprint(*args, **kwargs):
        print(*args, **kwargs, file=sys.stderr)
    dprint('debug mode')
except ModuleNotFoundError:

    def dprint(*args, **kwargs):
        pass
inId = 0
outId = 0
if inId > 0:
    dprint('use input', inId)
    sys.stdin = open('input' + str(inId) + '.txt', 'r')
if outId > 0:
    dprint('use output', outId)
    sys.stdout = open('stdout' + str(outId) + '.txt', 'w')
    atexit.register(lambda: sys.stdout.close())
(N, S) = getIntList()
za = getIntList()
za.sort()
mid = N // 2
res = 0
for i in range(N):
    if i < mid:
        if za[i] > S:
            res += za[i] - S
    elif i > mid:
        if za[i] < S:
            res += S - za[i]
    else:
        res += abs(S - za[i])
print(res)
