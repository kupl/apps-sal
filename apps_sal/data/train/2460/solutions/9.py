class Solution:

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if all((n < 0 for n in nums)):
            return max(nums)
        i = 0
        a = 0
        maxsum = 0
        while i < len(nums):
            b = c = 0
            while i < len(nums) and nums[i] <= 0:
                b += nums[i]
                i += 1
            while i < len(nums) and nums[i] >= 0:
                c += nums[i]
                i += 1
            a = max(a + b + c, c)
            maxsum = max(maxsum, a)
        return maxsum
