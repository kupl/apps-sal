class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                n.append((nums[i] - 1) * (nums[j] - 1))
        return max(n)
