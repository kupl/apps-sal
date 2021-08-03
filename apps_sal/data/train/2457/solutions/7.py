class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return -1
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        if nums[0] == sum:
            return 0
        left_sum = 0
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            if left_sum * 2 == sum - nums[i + 1]:
                return i + 1
        if nums[len(nums) - 1] == sum:
            return len(nums) - 1
        return -1
