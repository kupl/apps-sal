class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return nums[0]

        left = 0
        right = 0

        for i in range(1, len(nums)):
            right += nums[i]

        if left == right:
            return 0

        for i in range(1, len(nums)):
            left += nums[i - 1]
            right -= nums[i]

            if left == right:
                return i

        return -1
