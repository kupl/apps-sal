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

    def numSubmat(self, mat: List[List[int]]) -> int:
        R = len(mat)
        if not R:
            return 0
        C = len(mat[0])

        ans = [[0 for _ in range(C)] for _ in range(C)]

        cnt = 0

        for i in range(R):
            nextAns = [[0 for _ in range(C)] for _ in range(C)]
            last0j = -1
            for j in range(C):
                if not mat[i][j]:
                    last0j = j

                for si in range(last0j + 1, j + 1):
                    nextAns[j][si] = ans[j][si] + 1
                    cnt += nextAns[j][si]
                    #print(cnt, j, si)
            ans = nextAns

        return cnt

\"\"\"
S = Solution()
mat = [[1, 1]]
mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
mat = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]
mat = [[1, 1, 1, 1, 1, 1]]
mat = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
print(S.numSubmat(mat))
\"\"\"

