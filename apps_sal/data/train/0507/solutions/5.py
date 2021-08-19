class Solution:

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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
