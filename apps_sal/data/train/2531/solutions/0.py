class Solution:

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        size = len(nums)
        if size == 0:
            return 0
        while left < size and nums[left - 1] <= nums[left]:
            left += 1
        if left == size:
            return 0
        left -= 1
        right = size - 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1
        sub = nums[left:right + 1]
        min_ = min(sub)
        max_ = max(sub)
        for i in range(left):
            if nums[i] > min_:
                left = i
                break
        for i in range(size - 1, right, -1):
            if nums[i] < max_:
                right = i
                break
        return right - left + 1
