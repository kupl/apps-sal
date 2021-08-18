class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = min(nums)
        res = 0
        for i in nums:
            res += (i - m)
        return res
