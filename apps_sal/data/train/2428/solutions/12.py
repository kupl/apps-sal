class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        for i in range(len(nums)):
            if not (i + 1 < len(nums) and (nums[i] == nums[i + 1] or nums[i] == nums[i - 1])):
                return nums[i]
