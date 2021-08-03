class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current, the_max = [nums[0]] * 2
        for num in nums[1:]:
            current = max(num, current + num)
            the_max = max(current, the_max)
        return the_max
