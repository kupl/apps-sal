class Solution:

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return False
        d = {}
        for i in range(len(nums)):
            if nums[i] in d.keys() and abs(i - d[nums[i]]) <= k:
                return True
            else:
                d[nums[i]] = i
        return False
