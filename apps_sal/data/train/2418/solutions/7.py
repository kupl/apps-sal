class Solution:
    def containsDuplicate(self, nums):

        if len(nums) < 2:
            return False
        return True if len(set(nums)) < len(nums) else False

        """
         :type nums: List[int]
         :rtype: bool
         """
