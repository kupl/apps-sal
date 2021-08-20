from typing import List
import collections
import heapq
import itertools
import bisect


class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        s = sorted([a for (a, _) in requests])
        e = sorted([a for (_, a) in requests])
        freq = []
        for i in range(len(nums)):
            start_after = bisect.bisect_right(s, i)
            end_before = bisect.bisect_left(e, i)
            freq.append(start_after - end_before)
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        res = 0
        for (i, f) in enumerate(freq):
            res += int(f * nums[i] % (1000000000.0 + 7))
        return int(res % (1000000000.0 + 7))
