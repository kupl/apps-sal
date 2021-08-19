class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.quickSort(nums, 0, n - 1)
        return nums

    def quickSort(self, nums, low, high):
        if low < high:
            pivot = self.partition(nums, low, high)
            self.quickSort(nums, low, pivot - 1)
            self.quickSort(nums, pivot + 1, high)

    def partition(self, nums: List[int], low, high) -> int:
        i = low - 1
        pivot = nums[high]
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                (nums[i], nums[j]) = (nums[j], nums[i])
        (nums[i + 1], nums[high]) = (nums[high], nums[i + 1])
        return i + 1
