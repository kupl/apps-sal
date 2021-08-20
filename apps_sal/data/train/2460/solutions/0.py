class Solution:

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = csum = nums[0]
        for num in nums[1:]:
            if num >= csum + num:
                csum = num
            else:
                csum += num
            if csum > max_sum:
                max_sum = csum
        return max_sum
