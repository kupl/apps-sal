class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
         set_nums = set(nums)
         if len(set_nums) < len(nums):
             return True
         return False
         """
        dict1 = {}
        for num in nums:
            dict1[num] = dict1.get(num, 0) + 1

        for key in dict1:
            if dict1[key] > 1:
                return True
        return False
