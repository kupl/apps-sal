class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        running_min = nums[0]
        reduction = 0
        for i in nums:
            reduction += i
            running_min = min(running_min, reduction)

        return 1 if running_min >= 1 else 1 - running_min
