from random import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(start, end):
            pivot = round(random() * (end - start)) + start
            nums[start], nums[pivot] = nums[pivot], nums[start]
            below = above = start + 1
            while above <= end:
                if nums[above] <= nums[start]:
                    nums[below], nums[above] = nums[above], nums[below]
                    below += 1
                above += 1
            nums[below - 1], nums[start] = nums[start], nums[below - 1]
            return below - 1

        start = 0
        end = len(nums) - 1

        def quick_sort(start, end):
            if start < end:
                pivot = partition(start, end)
                quick_sort(start, pivot - 1)
                quick_sort(pivot + 1, end)

        quick_sort(start, end)

        return nums
