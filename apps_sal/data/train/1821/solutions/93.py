import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, arr, l, r):
        if l >= r:
            return

        position = self.partition(arr, l, r)
        self.quickSort(arr, l, position)
        self.quickSort(arr, position + 1, r)

    def partition(self, arr, l, r):
        pivot = arr[random.randint(l, r)]
        arr[l], pivot = pivot, arr[l]
        while l < r:
            while l < r and arr[r] >= pivot:
                r -= 1
            arr[l] = arr[r]
            while l < r and arr[l] <= pivot:
                l += 1
            arr[r] = arr[l]

            arr[l] = pivot
        return l
