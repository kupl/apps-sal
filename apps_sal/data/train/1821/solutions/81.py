class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # BASE CASE
        if not nums or len(nums) == 1:
            return nums

        pivot = nums[0]
        # pointer from 1 on
        # check if the pointer is <= pivot
        # if it is, then swap with the idx val, increment
        # if it is not, then skip, increment
        # that pointer is the spot where the pivot should be
        pivot_i = 1  # pivot_i, where pivot goes after sorting
        for i in range(1, len(nums)):
            if nums[i] <= pivot:
                nums[pivot_i], nums[i] = nums[i], nums[pivot_i]
                pivot_i += 1
        nums[pivot_i - 1], nums[0] = nums[0], nums[pivot_i - 1]
        # at pivot_i-1 is your pivot
        return self.sortArray(nums[:pivot_i - 1]) + [pivot] + self.sortArray(nums[pivot_i:])
