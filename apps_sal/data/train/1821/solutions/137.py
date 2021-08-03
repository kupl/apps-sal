def max_heapify(nums, i, lo, hi):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l <= hi and nums[i] < nums[l]:
        largest = l
    if r <= hi and nums[largest] < nums[r]:
        largest = r
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        max_heapify(nums, largest, lo, hi)


def build_max_heap(nums):
    for i in range(len(nums) // 2 - 1, -1, -1):
        max_heapify(nums, i, 0, len(nums) - 1)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        build_max_heap(nums)
        for i in range(len(nums) - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            max_heapify(nums, 0, 0, i - 1)
        return nums
