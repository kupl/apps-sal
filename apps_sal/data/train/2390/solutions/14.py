#   In this template you are not required to write code in main

import sys
inf = float("inf")

#from collections import deque, Counter, OrderedDict,defaultdict
#from heapq import nsmallest, nlargest, heapify,heappop ,heappush, heapreplace
#from math import ceil,floor,log,sqrt,factorial,pow,pi,gcd
#from bisect import bisect_left,bisect_right

abc = 'abcdefghijklmnopqrstuvwxyz'
abd = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
mod, MOD = 1000000007, 998244353
vow = ['a', 'e', 'i', 'o', 'u']
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()


Q = int(input())
while Q > 0:
    mydict1 = dict()
    n = int(input())
    a = get_array()
    for j in a:
        mydict1[j] = mydict1.get(j, 0) + 1
    ct = 0
    myset1 = set()
    for i in mydict1:
        if mydict1[i] not in myset1:
            ct += mydict1[i]
            myset1.add(mydict1[i])
        else:
            z = mydict1[i]
            for i in range(z, 0, -1):
                if i not in myset1:
                    ct += i
                    myset1.add(i)
                    break
    print(ct)
    Q -= 1
