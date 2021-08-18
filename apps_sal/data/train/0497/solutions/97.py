from functools import lru_cache


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if not startTime or not endTime or not profit:
            return 0

        intervals = list(zip(startTime, endTime, profit))
        intervals.sort(key=lambda x: x[0])

        def find_next_idx_binary_search(left, right, time):
            while left < right:
                mid = left + (right - left) // 2
                if intervals[mid][0] >= time:
                    right = mid
                else:
                    left = mid + 1
            return left

        @lru_cache(maxsize=None)
        def helper(idx):
            if idx == len(intervals) or idx < 0:
                return 0
            j = find_next_idx_binary_search(idx + 1, len(intervals), intervals[idx][1])
            return max(helper(j) + intervals[idx][2], helper(idx + 1))

        return helper(0)
