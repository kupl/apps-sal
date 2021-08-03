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

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        M = len(matrix[0])
        sigCnt = {}
        for i in range(N):
            if matrix[i][0]:
                for c in range(M):
                    matrix[i][c] = 1 - matrix[i][c]
            sig = \"\".join(map(str, matrix[i]))
            if not sig in sigCnt:
                sigCnt[sig] = 0
            sigCnt[sig] += 1
        return max(sigCnt.values())

\"\"\"
s = Solution()
l = [[0, 1], [1, 1]]
l = [[0, 1], [1, 0]]
l = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
print(s.maxEqualRowsAfterFlips(l))
\"\"\"

