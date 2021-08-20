class Solution:

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        num = [i for i in nums if i < target]
        return len(num)
