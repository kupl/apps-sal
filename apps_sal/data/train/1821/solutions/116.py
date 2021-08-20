class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(nums, low, high):
            p = nums[low]
            (i, j) = (low, low + 1)
            while j <= high:
                if p > nums[j]:
                    (nums[i + 1], nums[j]) = (nums[j], nums[i + 1])
                    i += 1
                j += 1
            (nums[i], nums[low]) = (nums[low], nums[i])
            return i

        def quickSort(nums, low, high):
            if low < high:
                pivot_ind = partition(nums, low, high)
                quickSort(nums, low, pivot_ind - 1)
                quickSort(nums, pivot_ind + 1, high)
        (low, high) = (0, len(nums) - 1)
        quickSort(nums, low, high)
        return nums
