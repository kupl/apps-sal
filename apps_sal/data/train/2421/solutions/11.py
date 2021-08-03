class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hist = {}
        for num in nums:
            if num not in hist:
                hist[num] = 0
            hist[num] += 1
            if hist[num] > len(nums) // 2:
                return num
