class Solution:

    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        lowest = nums[0]
        for num in nums:
            lowest = min(num, lowest)
        res = 0
        for num in nums:
            res += num - lowest
        return res
