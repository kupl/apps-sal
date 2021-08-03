class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        temp, res = 1, 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                temp += 1
            else:
                res = max(res, temp)
                temp = 1
        res = max(res, temp)
        return res
