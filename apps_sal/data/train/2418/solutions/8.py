class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == None or len(nums) <= 1:
            return False
        map = {}
        for i in nums:
            if i in map:
                return True
            else:
                map[i] = 0

        return False
