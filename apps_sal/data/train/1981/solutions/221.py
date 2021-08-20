from collections import Counter, deque
from itertools import chain
import heapq


class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        f = [0] * (len(nums) + 1)
        for (i, j) in requests:
            f[i] += 1
            f[j + 1] -= 1
        for i in range(1, len(nums) + 1):
            f[i] += f[i - 1]
        return sum((x * y for (x, y) in zip(sorted(f, reverse=True), sorted(nums, reverse=True)))) % (10 ** 9 + 7)
