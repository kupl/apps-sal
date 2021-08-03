class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        max1 = max(nums)
        idx = nums.index(max1)
        del nums[idx]
        max2 = max(nums)
        return idx if max2 * 2 <= max1 else -1
