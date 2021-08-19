class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        m = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                m = max(m, (nums[i] - 1) * (nums[j] - 1))
        return m
