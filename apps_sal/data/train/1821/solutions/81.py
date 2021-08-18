class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 1:
            return nums

        pivot = nums[0]
        pivot_i = 1
        for i in range(1, len(nums)):
            if nums[i] <= pivot:
                nums[pivot_i], nums[i] = nums[i], nums[pivot_i]
                pivot_i += 1
        nums[pivot_i - 1], nums[0] = nums[0], nums[pivot_i - 1]
        return self.sortArray(nums[:pivot_i - 1]) + [pivot] + self.sortArray(nums[pivot_i:])
