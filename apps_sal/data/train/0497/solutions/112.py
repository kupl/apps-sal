class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp = {}
        interval = []
        for i in range(len(startTime)):
            interval.append((endTime[i], startTime[i], profit[i]))
        interval.sort()
        ans = 0
        for j, i, p in interval:
            index = self.find_previous_end(interval, i)
            dp.setdefault(index, 0)
            dp[j] = max(dp[index] + p, ans)
            ans = max(ans, dp[j])
        return ans

    def find_previous_end(self, nums, target):
        l, r = 0, len(nums)
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid][0] > target:
                r = mid
            else:
                l = mid
        if nums[r][0] <= target:
            return nums[r][0]
        if nums[l][0] <= target:
            return nums[l][0]
        return 0
