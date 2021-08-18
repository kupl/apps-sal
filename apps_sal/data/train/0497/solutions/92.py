class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def search(dp, end):
            left, right = 0, len(dp) - 1
            while left < right:
                mid = left + (right - left + 1) // 2
                if dp[mid][0] <= end:
                    left = mid
                else:
                    right = mid - 1
            return left

        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for start, end, profit in jobs:
            pos = search(dp, start)
            if dp[pos][1] + profit > dp[-1][1]:
                dp.append([end, dp[pos][1] + profit])
        return dp[-1][1]
