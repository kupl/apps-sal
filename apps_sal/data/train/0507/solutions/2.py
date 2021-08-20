class Solution:

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        lo = 0
        hi = int(count / 2)
        while lo < hi:
            m = int((lo + hi) / 2)
            if nums[2 * m] != nums[2 * m + 1]:
                hi = m
            else:
                lo = m + 1
        return nums[2 * lo]
