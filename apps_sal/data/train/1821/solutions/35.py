
from collections import deque


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # heap sort
        # convert array to max heap
        for i in range(len(nums) // 2 - 1, -1, -1):
            self.heapify(nums, i, len(nums))
        # have pointer start at last element
        last = len(nums) - 1
        while last > 0:
            # swap last element with first element
            nums[last], nums[0] = nums[0], nums[last]
            # restore heap property from [:pointer]
            self.heapify(nums, 0, last)
            # decrement pointer
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


#     #     nums = deque(nums)
#     #     if len(nums) <= 1:
#     #         return nums
#     #     mid = len(nums) // 2
#     #     left = self.sortArray(nums[:mid])
#     #     right = self.sortArray(nums[mid:])
#     #     return self.merge(left, right)

#     # def merge(self, left, right):
#     #     merged = deque([])
#     #     while left and right:
#     #         merged.append(left.popleft() if left[0] < right[0] else right.popleft())
#     #     return merged + left + right

#     def sortArray(self, nums: List[int]) -> List[int]:
#         return self.merge_sort(nums, 0, len(nums) - 1)

#     def merge_sort(self, nums, start, end):
#         if end <= start:
#             return nums
#         mid = start + (end - start) // 2
#         self.merge_sort(nums, start, mid)
#         self.merge_sort(nums, mid + 1, end)
#         return self.merge(nums, start, mid, end)

#     def merge(self, nums, start, mid, end):
#         left, right = [], []
#         for i in range(start, mid + 1):
#             left.append(nums[i])
#         for j in range(mid + 1, end + 1):
#             right.append(nums[j])
#         i, j, k = 0, 0, start

#         # pick out smallest elements until smaller list is exhausted
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1

#         # copy remaining elements
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1
#         return nums
