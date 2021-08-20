class Solution:

    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_min = nums[0]
        res = 0
        for i in range(len(nums)):
            if nums[i] >= nums_min:
                res += nums[i] - nums_min
            else:
                res += i * (nums_min - nums[i])
                nums_min = nums[i]
        return res
