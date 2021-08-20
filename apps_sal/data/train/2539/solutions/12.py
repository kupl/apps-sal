class Solution:

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for num in range(len(nums) + 1):
            total += num
        return total - sum(nums)
