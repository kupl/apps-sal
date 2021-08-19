class Solution:

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[-1] < target:
            return len(nums)
        index = 0
        while nums[index] < target:
            index += 1
        return index
