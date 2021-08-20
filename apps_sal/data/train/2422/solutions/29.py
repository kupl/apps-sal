class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        max_val = float('-inf')
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                max_val = max(max_val, (nums[i] - 1) * (nums[j] - 1))
        return max_val
