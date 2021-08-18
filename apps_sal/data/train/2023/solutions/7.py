
from collections import defaultdict
import sys
import heapq
import bisect
import math
import itertools
import string
import queue
import datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]


def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())


N = int(input())
k = int(math.sqrt(N - 1)) + 1
ans = []
if N == 1:
    ans = [1]
elif N == 2:
    ans = [2, 1]
elif N == 3:
    ans = [2, 3, 1]
else:
    while N > 0:
        li = []
        for i in range(k):
            if N > 0:
                li.append(N)
            N -= 1
        li.reverse()
        ans = ans + li

print(' '.join(map(str, ans)))
