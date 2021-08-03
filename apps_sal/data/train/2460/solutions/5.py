class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, curr = nums[0], nums[0]
        i = 1
        while i < len(nums):
            curr = max(nums[i], curr + nums[i])
            result = max(curr, result)
            i += 1
        return result
