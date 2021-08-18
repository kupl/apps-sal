class Solution:
    def sortArray(self, nums: List[int]):

        self.qsort(nums, 0, len(nums) - 1)
        return nums

    def qsort(self, nums, start_idx, end_idx):

        if end_idx <= start_idx:
            return

        correct_idx = self.partition(nums, start_idx, end_idx)
        self.qsort(nums, start_idx, correct_idx - 1)
        self.qsort(nums, correct_idx + 1, end_idx)

    def partition(self, nums, start, end):
        pivot = nums[start]
        left = start + 1
        right = end

        while left <= right:

            if nums[left] > pivot and nums[right] < pivot:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            if nums[left] <= pivot:
                left += 1
            if nums[right] >= pivot:
                right -= 1

        nums[start], nums[right] = nums[right], nums[start]
        return right
