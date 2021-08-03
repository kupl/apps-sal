class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        left = [0]
        for num in nums:
            left.append(left[-1] + num)
        right = [0]
        for i in range(len(nums) - 1, -1, -1):
            right.append(right[-1] + nums[i])

        length = len(nums)
        for i in range(len(left) - 1):
            if left[i] == right[length - i - 1]:
                return i
        return -1
