class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        maxnum = max(nums)
        index = nums.index(maxnum)
        nums.sort()
        if nums[-1] >= nums[-2] * 2:
            return index
        else:
            return -1
