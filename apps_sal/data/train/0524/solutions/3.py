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
def data(): return sys.stdin.readline().strip()
def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var)) + end)
def L(): return list(sp())
def sl(): return list(ssp())
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]


try:
    sys.stdin = open("input.txt", "r")
except:
    pass


def pmat(A):
    for ele in A:
        print(*ele, end="\n")


def seive():
    prime = [1 for i in range(10**6 + 1)]
    prime[0] = 0
    prime[1] = 0
    for i in range(10**6 + 1):
        if(prime[i]):
            for j in range(2 * i, 10**6 + 1, i):
                prime[j] = 0
    return prime


s = list(sys.stdin.readline().strip())
n = len(s)
BIT = [[0] * (n + 1) for i in range(26)]


def update(i, idx, val):
    idx += 1
    while idx <= n:
        BIT[i][idx] += val
        idx += (-idx & idx)


def read(i, idx):
    ret = 0
    while idx > 0:
        ret += BIT[i][idx]
        idx -= (-idx & idx)
    return ret


for i in range(n):
    update(ord(s[i]) - 97, i, 1)

q = int(sys.stdin.readline())

for _ in range(q):
    a, b = sys.stdin.readline().split()
    t = 2
    if t == "1":
        idx = int(a) - 1
        bit_idx = ord(s[idx]) - 97
        update(bit_idx, idx, -1)
        s[idx] = b
        bit_idx = ord(b) - 97
        update(bit_idx, idx, 1)
    else:
        ans = 0
        l, r = int(a), int(b)
        for i in range(1, 26, 2):
            ans += 1 if (read(i, r) - read(i, l - 1)) > 0 else 0
        print(ans)


endtime = time.time()
