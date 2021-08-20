class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(nums):
            N = len(nums)
            if N < 2:
                return nums
            nums_left = merge_sort(nums[:N // 2])
            nums_right = merge_sort(nums[N // 2:])
            (i, j, k) = (0, 0, 0)
            while i < len(nums_left) and j < len(nums_right):
                if nums_left[i] <= nums_right[j]:
                    nums[k] = nums_left[i]
                    i += 1
                elif nums_left[i] > nums_right[j]:
                    nums[k] = nums_right[j]
                    j += 1
                k += 1
            while i < len(nums_left):
                nums[k] = nums_left[i]
                i += 1
                k += 1
            while j < len(nums_right):
                nums[k] = nums_right[j]
                j += 1
                k += 1
            return nums
        return merge_sort(nums)
