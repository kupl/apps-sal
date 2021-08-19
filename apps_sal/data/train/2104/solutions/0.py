import bisect
import collections
import atexit
import math
import sys
from functools import cmp_to_key
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


def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def comb(n, k):
    if k == 0:
        return 1
    if n == k:
        return 1
    return comb(n - 1, k - 1) + comb(n - 1, k)


inId = 0
outId = 0
if inId > 0:
    dprint('use input', inId)
    sys.stdin = open('input' + str(inId) + '.txt', 'r')
if outId > 0:
    dprint('use output', outId)
    sys.stdout = open('stdout' + str(outId) + '.txt', 'w')
    atexit.register(lambda: sys.stdout.close())
(N,) = getIntList()
zz = getIntList()
zz.sort()
result = (zz[N - 1] - zz[0]) * (zz[2 * N - 1] - zz[N])
dif = zz[2 * N - 1] - zz[0]
for i in range(N):
    nd = zz[i + N - 1] - zz[i]
    result = min(result, nd * dif)
print(result)
