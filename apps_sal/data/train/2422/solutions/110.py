class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = 0
        num_len = len(nums)
        for i in range(num_len):
            for j in range(i, num_len):
                product = (nums[i] - 1) * (nums[j] - 1)
                if i != j and product > max_product:
                    max_product = product
        return max_product
