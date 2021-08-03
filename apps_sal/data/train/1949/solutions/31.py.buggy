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
\"\"\"
\"\"\"


def dfs(r, c, grid):
    ans = grid[r][c]
    temp = ans
    grid[r][c] = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for i in range(4):
        newr = r + dr[i]
        newc = c + dc[i]
        if newr >= 0 and newr < len(grid) and newc >= 0 and newc < len(
                grid[0]) and grid[newr][newc]:
            #print(r, c, newr, newc)
            ans = max(ans, temp + dfs(newr, newc, grid))
    grid[r][c] = temp
    return ans


class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        ans = 0
        for r in range(N):
            for c in range(M):
                if grid[r][c]:
                    ans = max(ans, dfs(r, c, grid))
        return ans

\"\"\"
sol = Solution()
grid = [[0, 1, 0], [2, 3, 4]]
grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
print(sol.getMaximumGold(grid))
\"\"\"
