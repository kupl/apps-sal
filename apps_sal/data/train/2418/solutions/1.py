class Solution:

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '\n         set_nums = set(nums)\n         if len(set_nums) < len(nums):\n             return True\n         return False\n         '
        dict1 = {}
        for num in nums:
            dict1[num] = dict1.get(num, 0) + 1
        for key in dict1:
            if dict1[key] > 1:
                return True
        return False
