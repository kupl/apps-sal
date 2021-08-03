class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums) + 1
        total = sum(i for i in range(length))

        nums_total = sum(nums)

        return total - nums_total
