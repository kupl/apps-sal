class Solution:

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ymax = [nums[i] for i in range(len(nums))]
        nmax = [nums[i] for i in range(len(nums))]
        nmax[0] = 0
        if len(nums) > 1:
            ymax[1] = max(ymax[0], ymax[1])
        for i in range(2, len(nums)):
            if i == len(nums) - 1:
                ymax[i] = ymax[i - 1]
            else:
                ymax[i] = max(ymax[i - 1], ymax[i - 2] + ymax[i])
            nmax[i] = max(nmax[i - 1], nmax[i - 2] + nmax[i])
        return max(nmax[-1], ymax[-1])
