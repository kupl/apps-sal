class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quicksort(nums)

    def quicksort(self, nums):
        if len(nums) == 1 or len(nums) == 0:
            return nums
        pivot = nums[len(nums) // 2]
        left = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        return self.quicksort(left) + mid + self.quicksort(right)
