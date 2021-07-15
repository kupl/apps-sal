import sys, math,os
from io import BytesIO, IOBase
#from bisect import bisect_left as bl, bisect_right as br, insort
#from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
#from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var) : sys.stdout.write(' '.join(map(str, var))+'\n')
def out(var) : sys.stdout.write(str(var)+'\n')
sys.setrecursionlimit(100000)
INF = float('inf')
mod = int(1e9)+7


def main():

    for t in range(int(data())):
        a,b=mdata()
        print(max(a,b,2*min(a,b))**2)

def __starting_point():
    main()
__starting_point()
