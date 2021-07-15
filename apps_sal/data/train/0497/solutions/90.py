from typing import List
from functools import lru_cache
from bisect import bisect

class Solution:
    
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        n = len(intervals)
        
        @lru_cache(None)
        def helper(idx):
            if idx >= n:
                return 0
            start, end, profit = intervals[idx]
            not_take_option = helper(idx + 1)
            take_option = profit + helper(bisect(intervals, (end,)))
            return max(not_take_option, take_option)
        
        return helper(0)
