class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        pivot = nums[0]
        left = [x for x in nums[1:] if x <= pivot]
        right = [x for x in nums[1:] if x > pivot]
        return self.sortArray(left) + [pivot] + self.sortArray(right)
