class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_product = (nums[0] - 1) * (nums[1] - 1)
        for i in range(n - 1):
            for j in range(i + 1, n):
                product = (nums[i] - 1) * (nums[j] - 1)
                if product > max_product:
                    max_product = product
        return max_product
