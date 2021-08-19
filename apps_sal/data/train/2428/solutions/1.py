class Solution:

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = 0
        for n in nums:
            single ^= n
        return single
