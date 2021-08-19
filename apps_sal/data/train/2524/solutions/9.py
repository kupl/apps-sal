class Solution:

    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_count = 0
        max_count = 0
        for (index, num) in enumerate(nums):
            current_count += 1
            if index < len(nums) - 1:
                if num >= nums[index + 1]:
                    max_count = max(max_count, current_count)
                    current_count = 0
        return max(max_count, current_count)
