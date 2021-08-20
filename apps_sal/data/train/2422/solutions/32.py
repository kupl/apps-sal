class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        max_prod = 0
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                prod = (nums[i] - 1) * (nums[j] - 1)
                max_prod = max(max_prod, prod)
        return max_prod
