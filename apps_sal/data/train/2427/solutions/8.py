class Solution:

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                sum += 1
            else:
                sum = 0
            if sum > max:
                max = sum
            else:
                max = max
        return max
