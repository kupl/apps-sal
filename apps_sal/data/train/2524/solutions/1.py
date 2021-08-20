class Solution:

    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        result = 1
        max_result = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                result += 1
                if result > max_result:
                    max_result = result
            else:
                result = 1
        return max_result
