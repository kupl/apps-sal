class Solution:

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_c = 0
        cur = 0
        for n in nums:
            if n == 1:
                cur += 1
            if n == 0:
                max_c = max(max_c, cur)
                cur = 0
        max_c = max(max_c, cur)
        return max_c
