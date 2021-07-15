from collections import Counter
import math
import sys
from bisect import bisect,bisect_left,bisect_right
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def mod(): return 10**9+7
 
for i in range(INT()): 
    n = INT()
    #s = input()
    #n,m = MAP()
    arr = LIST()
    d = {}
    for i in arr:
        if i in d:
            continue
        else:
            d[i] = 1
    ans = []
    for i in d:
        ans.append(i)
    print(*ans)

