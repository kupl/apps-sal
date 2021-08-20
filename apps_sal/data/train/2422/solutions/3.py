class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        prods = []
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                prods.append((nums[i] - 1) * (nums[j] - 1))
        return max(prods)
