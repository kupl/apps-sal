class Solution:

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        for n in set(nums):
            if nums.count(n) > l / 2:
                return n
