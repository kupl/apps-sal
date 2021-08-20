from math import *
from collections import *
from itertools import *
from bisect import *
from heapq import *
from operator import *
from sys import *
setrecursionlimit(1000000)
d = defaultdict(lambda: 0, {})


def io():
    return map(int, input().split())


def op():
    return list(map(int, input().split()))


def o():
    return int(input())


def r(x):
    if type(x) == int:
        return range(x)
    else:
        return range(len(x))


def kl(con, x=0):
    if x == 0:
        print('Yes') if con else print('No')
    elif x == 1:
        print('yes') if con else print('no')
    elif x == 2:
        print('YES') if con else print('NO')


MOD = 1000000007
MAX = float('inf')
MIN = -float('inf')
p = input
for _ in r(o()):
    (n, k) = io()
    l = op()
    ans = 0
    for i in r(l):
        for j in r(l):
            if l[i] > l[j]:
                if i > j:
                    ans += k * (k - 1) / 2
                elif i < j:
                    ans += k * (k + 1) / 2
    print(int(ans))
