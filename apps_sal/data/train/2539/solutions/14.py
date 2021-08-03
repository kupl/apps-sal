class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        srted = sorted(nums)

        for i in range(0, len(srted)):
            if srted[i] != i:
                return i

        return i + 1
