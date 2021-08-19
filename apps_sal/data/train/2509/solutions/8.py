class Solution:

    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        smallest = min(nums)
        for num in nums:
            count += abs(num - smallest)
        return count
