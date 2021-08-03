class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if max < (nums[i] - 1) * (nums[j] - 1):
                    max = (nums[i] - 1) * (nums[j] - 1)
        return max
