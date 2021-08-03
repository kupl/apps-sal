class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # O(N) time complexity O(1) space using bit XOR manipulation
        # x = nums[0]
        # for num in nums[1:]:
        #     x = x^num
        # return x

        # O(logN) runtime and O(1) Space using cool binary search (it's sorted)
        # focuses on the index

        left = 0
        if len(nums) == 1:
            return nums[left]

        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if mid % 2 == 1:
                mid -= 1

            if nums[mid + 1] == nums[mid]:
                left = mid + 2

            else:
                right = mid

        return nums[left]
