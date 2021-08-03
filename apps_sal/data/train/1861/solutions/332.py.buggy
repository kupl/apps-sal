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

    def minAreaRect(self, points: List[List[int]]) -> int:
        s = set()
        for p in points:
            s.add((p[0], p[1]))

        N = len(points)
        ans = 0
        for i in range(N):
            p1 = points[i]
            for j in range(i + 1, N):
                p2 = points[j]
                if p1[0] == p2[0] or p1[1] == p2[1]:
                    continue
                newA = abs(p1[0] - p2[0]) * abs(p1[1] - p2[1])
                if (ans == 0 or
                        newA < ans) and (p1[0], p2[1]) in s and (p2[0],
                                                                 p1[1]) in s:
                    ans = newA
        return ans

\"\"\"
l = [[1, 1], [1, 2]]
S = Solution()
l = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
l = [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
print(S.minAreaRect(l))
\"\"\"
