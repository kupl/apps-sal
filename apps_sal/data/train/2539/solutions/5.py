class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for i, x in enumerate(nums):
            res ^= i
            res ^= x
        return res
