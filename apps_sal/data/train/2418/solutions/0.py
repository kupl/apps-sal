class Solution:

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set(nums)
        if len(nums) == len(num_set):
            return False
        return True
