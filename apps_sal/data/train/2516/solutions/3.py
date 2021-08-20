class Solution:

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums == None or len(nums) <= 1 or k == 0:
            return False
        maps = {}
        for (i, item) in enumerate(nums):
            if item in maps and abs(maps[item] - i) <= k:
                return True
            else:
                maps[item] = i
        return False
