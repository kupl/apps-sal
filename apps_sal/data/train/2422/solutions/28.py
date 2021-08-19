class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        r = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                r = max(r, (nums[i] - 1) * (nums[j] - 1))
        return r
