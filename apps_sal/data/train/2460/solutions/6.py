class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = maxGlobalSum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i] + maxSum:
                maxSum = nums[i]
            else:
                maxSum += nums[i]

            if maxSum > maxGlobalSum:
                maxGlobalSum = maxSum

        return maxGlobalSum
