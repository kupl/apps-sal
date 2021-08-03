class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        dp = [0] * len(nums)

        for i in range(len(requests)):
            dp[requests[i][0]] += 1
            if requests[i][1] < len(nums) - 1:
                dp[requests[i][1] + 1] -= 1

        for i in range(1, len(dp)):
            dp[i] += dp[i - 1]

        dp.sort(reverse=True)
        nums.sort(reverse=True)
        ans = 0
        mod = int(1e9) + 7
        for i in range(len(nums)):
            ans += nums[i] * dp[i]
            ans = ans % mod

        return ans
