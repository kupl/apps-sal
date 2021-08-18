
from collections import deque


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        ans = []
        while left and right:
            ans.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        return ans + left + right
