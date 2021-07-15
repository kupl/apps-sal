'''
自宅用PCでの解答
'''
import math
#import numpy as np
import itertools
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9+7 #998244353
dir = [(-1,0),(0,-1),(1,0),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"

def main():
    n = int(ipt())
    ans = [0]*n
    a = [int(i) for i in ipt().split()]
    cts = [(a[0],0)]
    d = defaultdict(int)
    d[a[0]] = 1
    tot = a[0]
    for i,ai in enumerate(a[1::]):
        tot += ai
        d[ai] += 1
        if cts[-1][0] < ai:
            cts.append((ai,i+1))

#    print(d,cts)
    nms = sorted(list(d.keys()),reverse=True)
    lc = len(cts)-1
    na = cts[lc][0]
    ps = cts[lc][1]
    sm = 0
    for i in nms:
        sm += d[i]
        if i == na:
            lc -= 1
            na = cts[lc][0]
            ans[ps] += sm*(i-na)
            pps = ps
            ps = cts[lc][1]
        else:
            ans[pps] += d[i]*(i-na)
#        print(ans)

    ans[0] = tot-sum(ans[1::])

    for i in ans:
        print(i)



    return None

def __starting_point():
    main()

__starting_point()
