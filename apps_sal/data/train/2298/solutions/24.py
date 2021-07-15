from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
from typing import Union
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,t = inpl()
a = inpl()
m = []
mi = INF
for i in range(n-1):
    mi = min(mi, a[i])
    m.append(a[i+1]-mi)
print(m.count(max(m)))
