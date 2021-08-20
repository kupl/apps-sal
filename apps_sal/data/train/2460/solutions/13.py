class Solution:

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        sum_list = [0] * len(nums)
        sum_list[0] = max_sum
        for i in range(1, len(nums)):
            sum_list[i] = max(nums[i], sum_list[i - 1] + nums[i])
            max_sum = max(max_sum, sum_list[i])
        return max_sum
