class Solution:

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        (i, j) = (0, len(nums) - 1)
        while i < j:
            mid = i + (j - i) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                i = mid + 2
            else:
                j = mid
        return nums[i]
