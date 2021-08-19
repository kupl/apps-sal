class Solution(object):

    def findUnsortedSubarray(self, nums):
        nums = [float('-inf')] + nums + [float('inf')]
        'find left boundary'
        left = 0
        while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
            left += 1
        if left == len(nums) - 1:
            return 0
        min_num = min(nums[left + 1:])
        while nums[left] > min_num:
            left -= 1
        'find right boundary'
        right = len(nums) - 1
        while right > 0 and nums[right - 1] <= nums[right]:
            right -= 1
        if right == 0:
            return 0
        max_num = max(nums[:right])
        while nums[right] < max_num:
            right += 1
        return right - left - 1
