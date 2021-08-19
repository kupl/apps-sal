class Solution:

    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        Max = max(nums)
        if nums.count(Max) > 1:
            return -1
        if any(nums) == False:
            return 0
        if nums.count(0) == len(nums) - 1:
            return nums.index(Max)
        for i in nums:
            if i != Max and i != 0:
                if Max / i < 2:
                    return -1
        return nums.index(Max)
