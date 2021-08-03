class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.qs(nums, 0, len(nums) - 1)
        return nums

    def qs(self, nums, start, end):
        if start >= end:
            return

        pivot = nums[(start + end) // 2]

        left, right = start, end

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.qs(nums, start, right)
        self.qs(nums, left, end)
