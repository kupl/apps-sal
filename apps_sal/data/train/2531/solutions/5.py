class Solution:

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums_sorted = sorted(nums)
        is_same = [a == b for (a, b) in zip(nums, nums_sorted)]
        return 0 if all(is_same) else n - is_same.index(False) - is_same[::-1].index(False)
