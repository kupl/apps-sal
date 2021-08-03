from math import floor
from math import ceil
from math import sqrt
from collections import deque
import numpy
from _collections import deque
#from _ast import Num # LC doesn't like this
from heapq import *
from typing import List
import random

MOD = int(1e9 + 7)
BASE = 256


class Solution:

    def findTheCity(self, n: int, edges: List[List[int]],
                    distanceThreshold: int) -> int:
        minD = [[-1 for i in range(n)] for i in range(n)]
        for v in range(n):
            minD[v][v] = 0
        for e in edges:
            u = e[0]
            v = e[1]
            w = e[2]
            minD[u][v] = w
            minD[v][u] = w

        for midNode in range(n):
            for u in range(n):
                for v in range(n):
                    fh = minD[u][midNode]
                    sh = minD[midNode][v]
                    if fh >= 0 and sh >= 0:
                        if minD[u][v] < 0 or fh + sh < minD[u][v]:
                            minD[u][v] = fh + sh
        #print(minD)
        ans = 0
        minCnt = n + 1
        for u in range(n):
            cnt = 0
            for v in range(n):
                if minD[u][v] >= 0 and minD[u][v] <= distanceThreshold:
                    cnt += 1
        #   print(u, cnt)
            if cnt <= minCnt:
                minCnt = cnt
                ans = u
        return ans

\"\"\"
n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4
n = 5
edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
distanceThreshold = 2
s = Solution()
print(s.findTheCity(n, edges, distanceThreshold))
\"\"\"
