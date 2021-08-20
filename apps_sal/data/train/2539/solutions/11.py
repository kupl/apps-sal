class Solution:

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import functools
        res1 = functools.reduce(lambda x, y: x ^ y, [i for i in range(len(nums) + 1)])
        res2 = functools.reduce(lambda x, y: x ^ y, nums)
        return res1 ^ res2
