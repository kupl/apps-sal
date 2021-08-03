class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LCIS = 0
        i = 0
        j = 1
        while j <= len(nums):
            if j == len(nums) or nums[j - 1] >= nums[j]:
                l = j - i
                if LCIS < l:
                    LCIS = l
                i = j
            j += 1
        return LCIS
