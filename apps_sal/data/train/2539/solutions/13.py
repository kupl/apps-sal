class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = [0] * (len(nums) + 1)
        for e in nums:
            x[e] = 1
        return x.index(0)
