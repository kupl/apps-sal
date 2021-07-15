from typing import List
import collections
import heapq
import itertools
import bisect


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        s = sorted([a for a, _ in requests])
        e = sorted([a for _, a in requests])
        freq = []
        for i in range(len(nums)):
            start_after = bisect.bisect_right(s, i)
            end_before = bisect.bisect_left(e, i)
            # print(start_after, end_before)
            # in_it = int(start_after == end_before and start_after < len(requests) and )
            freq.append(start_after - end_before)
        # print(freq)
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        res = 0
        for i, f in enumerate(freq):
            res += int(f * nums[i] % (1e9 + 7))
        return int(res % (1e9 + 7))

