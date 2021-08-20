class Solution:

    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = max(nums)
        for n in nums:
            if 2 * n > largest and n != largest:
                return -1
        return nums.index(largest)
