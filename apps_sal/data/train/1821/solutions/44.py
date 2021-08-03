
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
