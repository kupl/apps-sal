class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        print(jobs)

        dp = [0] * len(jobs)
        dp[0] = jobs[0][-1]
        for i in range(1, len(dp)):
            curProfit = jobs[i][-1]
            j = self.searchInsert(jobs, jobs[i][0])
            if j != -1:
                curProfit += dp[j]
            dp[i] = max(dp[i - 1], curProfit)
        return dp[-1]

    def searchInsert(self, nums, target: int) -> int:
        if not nums:
            return 0

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m][1] == target:
                return m
            elif nums[m][1] < target:
                l = m + 1
            else:
                r = m - 1
        return l - 1
