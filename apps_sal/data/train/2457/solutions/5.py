class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot = sum(nums)
        n = tot
        for i in range(0, len(nums)):
            n = n - nums[i]
            if (tot - nums[i]) / 2 == n:
                return i
        return -1
