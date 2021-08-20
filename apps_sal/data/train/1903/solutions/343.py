from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import heapq
import string
true = True
false = False
(MIN, MAX, MOD) = (-1061109567, 1061109567, 1000000007)


class Solution:

    def minCostConnectPoints(self, ps: List[List[int]]) -> int:
        n = len(ps)
        if n < 2:
            return 0
        (keys, visited) = ([MAX] * n, [False] * n)
        keys[0] = 0
        cost = 0
        for _ in range(n):
            (idx, n_min) = (0, MAX)
            for j in range(n):
                if not visited[j] and keys[j] < n_min:
                    (idx, n_min) = (j, keys[j])
            visited[idx] = True
            cost += n_min
            for j in range(n):
                if not visited[j]:
                    weight = abs(ps[idx][0] - ps[j][0]) + abs(ps[idx][1] - ps[j][1])
                    if weight < keys[j]:
                        keys[j] = weight
        return cost


sol = Solution()
points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
