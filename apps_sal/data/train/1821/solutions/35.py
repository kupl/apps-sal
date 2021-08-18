
from collections import deque


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) // 2 - 1, -1, -1):
            self.heapify(nums, i, len(nums))
        last = len(nums) - 1
        while last > 0:
            nums[last], nums[0] = nums[0], nums[last]
            self.heapify(nums, 0, last)
            last -= 1
        return nums

    def heapify(self, nums, start, size):
        largest = start
        left = start * 2 + 1
        right = start * 2 + 2

        if left < size and nums[largest] < nums[left]:
            largest = left

        if right < size and nums[largest] < nums[right]:
            largest = right

        if largest != start:
            nums[start], nums[largest] = nums[largest], nums[start]
            self.heapify(nums, largest, size)
