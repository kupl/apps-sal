class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minx = min(nums)
        sums = sum(nums)
        return sums - len(nums) * minx
