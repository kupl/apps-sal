'''
研究室PCでの解答
'''
import math
#import numpy as np
import queue
import bisect
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9 + 7
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
alp = "abcdefghijklmnopqrstuvwxyz"


def main():
    n = int(ipt())
    ans = 0
    bmi = 10**18
    sm = 0
    for i in range(n):
        a, b = list(map(int, ipt().split()))
        sm += a
        if a > b and bmi > b:
            bmi = b
    if bmi == 10**18:
        print((0))
    else:
        print((sm - bmi))

    return None


def __starting_point():
    main()


__starting_point()
