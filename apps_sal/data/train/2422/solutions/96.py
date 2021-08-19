class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        curr_product = 0
        max_product = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if i == 0 and j == 0:
                    max_product = (nums[i] - 1) * (nums[j] - 1)
                else:
                    curr_product = (nums[i] - 1) * (nums[j] - 1)
                    if curr_product > max_product:
                        max_product = curr_product
        return max_product
