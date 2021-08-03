class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = 0
        for n in range(len(nums) - 1):
            for m in range(n + 1, len(nums)):
                product = (nums[n] - 1) * (nums[m] - 1)
                if product > result:
                    result = product
        return result
