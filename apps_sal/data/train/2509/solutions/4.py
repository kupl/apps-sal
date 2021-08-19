class Solution:

    def minMoves(self, nums):
        s = sum(nums)
        minimum = min(nums)
        n = len(nums)
        result = s - minimum * n
        return result
