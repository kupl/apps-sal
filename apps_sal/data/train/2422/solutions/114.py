class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                l.append((nums[i] - 1) * (nums[j] - 1))
        return max(l)
