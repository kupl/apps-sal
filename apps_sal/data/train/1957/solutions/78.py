from typing import List
from functools import lru_cache
import collections
import heapq
import itertools
import bisect
import copy
import random
import re
import fractions
import math
import functools

mod = 10 ** 9 + 7


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not len(grid) or not len(grid[0]):
            return 0
        m, n = len(grid), len(grid[0])

        def neighbors(i, j):
            for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ni < m and 0 <= nj < n:
                    yield ni, nj

        start = (0, 0, k)
        seen = {start}
        q = collections.deque([(0, start)])
        while q:
            step, (i, j, k) = q.popleft()
            if (i, j) == (m - 1, n - 1):
                return step
            for ni, nj in neighbors(i, j):
                nk = k - grid[ni][nj]
                state = (ni, nj, nk)
                if nk >= 0 and state not in seen:
                    q.append((step + 1, state))
                    seen.add(state)

        return -1
