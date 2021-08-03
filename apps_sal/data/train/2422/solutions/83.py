class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] - 1) * (nums[j] - 1) > prod:
                    prod = (nums[i] - 1) * (nums[j] - 1)
        return prod
