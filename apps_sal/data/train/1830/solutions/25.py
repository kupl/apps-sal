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


class DisjointSet:

    def __init__(self, size=10):
        self.data = list(range(size))

    def find(self, i):
        if i == self.data[i]:
            return i
        else:
            j = self.find(self.data[i])
            self.data[i] = j
            return j

    def merge(self, i):
        self.data[i] = i + 1


class Solution:

    def method2(self, rains: List[int]) -> List[int]:
        n = len(rains)
        cc = {}
        ds = DisjointSet(n)
        i = 0
        while i < n:
            if rains[i] == 0:
                rains[i] = 1
            else:
                lake = rains[i]
                if lake in cc:
                    available_dry_day = ds.find(cc[lake])
                    if available_dry_day < i:
                        rains[available_dry_day] = lake
                        ds.merge(available_dry_day)
                    else:
                        return []
                cc[lake] = i
                ds.merge(i)
                rains[i] = -1
            i += 1
        return rains

    def avoidFlood(self, rains: List[int]) -> List[int]:
        return self.method2(rains)
        n = len(rains)
        cc = defaultdict(int)
        dry = list()
        res = []
        for (i, r) in enumerate(rains):
            if r == 0:
                dry.append(i)
                res.append(1)
            else:
                if r not in cc:
                    cc[r] = i
                else:
                    last_idx = cc[r]
                    j = bisect_left(dry, last_idx)
                    if j == len(dry):
                        return []
                    day = dry[j]
                    del dry[j]
                    res[day] = r
                    cc[r] = i
                res.append(-1)
        return res


sol = Solution()
rains = [1, 2, 3, 4]
rains = [69, 0, 0, 0, 69]
rains = [1, 0, 2, 3, 0, 1, 2]
rains = [1, 2, 0, 0, 2, 1]
