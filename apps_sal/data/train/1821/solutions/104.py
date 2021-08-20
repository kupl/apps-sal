class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        return merge_sort(nums)


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = len(nums) // 2
    left = merge_sort(nums[:pivot])
    right = merge_sort(nums[pivot:])
    return merge(left, right)


def merge(l1: List[int], l2: List[int]) -> List[int]:
    res = []
    (i, j) = (0, 0)
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    while i < len(l1):
        res.append(l1[i])
        i += 1
    while j < len(l2):
        res.append(l2[j])
        j += 1
    return res
