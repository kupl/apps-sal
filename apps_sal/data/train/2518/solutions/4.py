class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        idx = -1
        if len(nums) >= 2:
            if nums[0] > nums[1]:
                r = 0
            else:
                r = 1
        for i in range(2, len(nums)):
            if nums[i] < nums[i - 1]:
                r = r - 1
                if nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
            if r < 0:
                return False
        return True
