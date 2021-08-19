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
# from sys import stdin
# input = stdin.readline
def data(): return sys.stdin.readline().strip()
def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var)) + end)
def L(): return list(sp())
def sl(): return list(ssp())
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]


try:
    # sys.setrecursionlimit(int(pow(10,6)))
    sys.stdin = open("input.txt", "r")
    # sys.stdout = open("../output.txt", "w")
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


prime = seive()
for _ in range(L()[0]):
    n = L()[0]
    if(n == 1):
        print("Grinch")
    elif(n == 2):
        print("Me")
    elif(n % 2 == 1):
        print("Me")
    else:
        x = n
        while(x % 2 == 0):
            x //= 2

        if(x == 1):
            print("Grinch")
        else:
            if (n // 2) % 2 == 0:
                print("Me")
            else:
                k = 0
                for i in range(3, 10**5):
                    if(prime[i] and x % i == 0):
                        while(x % i == 0):
                            x //= i
                            k += 1
                if(x != 1):
                    k += 1
                if(k <= 1):
                    print("Grinch")
                else:
                    print("Me")


endtime = time.time()
# print(f"Runtime of the program is {endtime - starttime}")
