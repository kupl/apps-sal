# class Solution:
#     def specialArray(self, nums: List[int]) -> int:
#         nums.sort(reverse=True)
#         left, right = 0, len(nums)
#         while left < right:
#             mid = left + (right - left) // 2
#             if mid < nums[mid]:
#                 left = mid + 1
#             else:
#                 right = mid
#         return -1 if left < len(nums) and left == nums[left] else left
class Solution:
    def specialArray(self, a: List[int]) -> int:
        n, i = len(a), 0
        a.sort(reverse=True)
        l, r = 0, n
        while l < r:
            m = l + (r - l) // 2
            if m < a[m]:
                l = m + 1
            else:
                r = m
        return -1 if l < n and l == a[l] else l
