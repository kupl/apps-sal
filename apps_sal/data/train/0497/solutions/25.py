from typing import List
from functools import lru_cache


class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        n = len(intervals)

        def get_next_idx(start_idx, end_time):
            (lo, hi, res) = (start_idx, n - 1, n)
            while lo <= hi:
                mid = (hi + lo) // 2
                start_time = intervals[mid][0]
                if start_time >= end_time:
                    (res, hi) = (mid, mid - 1)
                else:
                    lo = mid + 1
            return res

        @lru_cache(None)
        def helper(idx):
            if idx >= n:
                return 0
            (start, end, profit) = intervals[idx]
            not_take_option = helper(idx + 1)
            take_option = profit + helper(get_next_idx(idx + 1, end))
            return max(not_take_option, take_option)
        return helper(0)
