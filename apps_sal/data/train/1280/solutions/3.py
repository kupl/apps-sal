import sys
from functools import lru_cache, cmp_to_key
from heapq import merge, heapify, heappop, heappush
from math import *
from collections import defaultdict as dd, deque, Counter as C
from itertools import combinations as comb, permutations as perm
from bisect import bisect_left as bl, bisect_right as br, bisect
from time import perf_counter
from fractions import Fraction
import copy
import time
starttime = time.time()
mod = int(pow(10, 9) + 7)
mod2 = 998244353


def data():
    return sys.stdin.readline().strip()


def out(*var, end='\n'):
    sys.stdout.write(' '.join(map(str, var)) + end)


def L():
    return list(sp())


def sl():
    return list(ssp())


def sp():
    return map(int, data().split())


def ssp():
    return map(str, data().split())


def l1d(n, val=0):
    return [val for i in range(n)]


def l2d(n, m, val=0):
    return [l1d(n, val) for j in range(m)]


try:
    sys.stdin = open('input.txt', 'r')
except:
    pass


def pmat(A):
    for ele in A:
        print(*ele, end='\n')


def seive():
    prime = [1 for i in range(10 ** 6 + 1)]
    prime[0] = 0
    prime[1] = 0
    for i in range(10 ** 6 + 1):
        if prime[i]:
            for j in range(2 * i, 10 ** 6 + 1, i):
                prime[j] = 0
    return prime


for _ in range(L()[0]):
    s = input().strip()
    n = len(s)
    ans = 0
    for i in range((n - n % 2) // 2):
        ans += abs(ord(s[i]) - ord(s[n - 1 - i]))
    print(ans)
endtime = time.time()
