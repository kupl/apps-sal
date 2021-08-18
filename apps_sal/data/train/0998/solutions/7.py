'''

          Online Python Compiler.
       Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import sys
import os
import math
import copy
from bisect import bisect
from io import BytesIO, IOBase
from collections import deque, Counter, defaultdict
from itertools import permutations, combinations


def Int(): return int(sys.stdin.readline())
def Mint(): return map(int, sys.stdin.readline().split())
def Lstr(): return list(sys.stdin.readline().strip())
def Str(): return sys.stdin.readline().strip()
def Mstr(): return map(str, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().split()))
def Hash(): return dict()
def Mod(): return 1000000007
def Ncr(n, r, p): return ((fact[n]) * ((ifact[r] * ifact[n - r]) % p)) % p
def Most_frequent(list): return max(set(list), key=list.count)
def Mat2x2(n): return [List() for _ in range(n)]


def solution():
    n, k = map(int, input().split())
    m = -float('inf')
    a = [0 for i in range(n)]
    b = [0 for i in range(n)]
    for i in range(k):
        q, r, e = map(str, input().split())
        r, e = int(r), int(e)
        if q[0] == 'R':
            a[r - 1] += e
        else:
            b[r - 1] += e
    print(str(max(a) + max(b)) + '\n')


def __starting_point():
    solution()


__starting_point()
