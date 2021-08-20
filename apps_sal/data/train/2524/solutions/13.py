class Solution:

    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        for i in range(len(nums)):
            if nums[i - 1] >= nums[i]:
                anchor = i
            ans = max(ans, i - anchor + 1)
        return ans
