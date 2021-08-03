from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
from collections import deque, defaultdict, Counter
import sys
input = sys.stdin.readline


def SI(): return input()


def NI(): return int(input())
def MI(): return map(int, input().split())


def cutLF(x): return list(x)[:-1] if x[-1] == '\n' else list(x)
def strLST(): return cutLF(input())


n, m = MI()
*a, = MI()
s = sum(a)
mod = 10**9 + 7
hidari = []
start = n + m
for i in range(n + s):
    hidari.append(start - i)

left = 1
right = 1
for i in range(n + s):
    left *= hidari[i]
    left %= mod
    right *= (i + 1)
    right %= mod

print(left * pow(right, mod - 2, mod) % mod)
