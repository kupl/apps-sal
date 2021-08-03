class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p = []
        for count, n in enumerate(nums):
            for i in range(count + 1, len(nums)):
                p.append((nums[i] - 1) * (n - 1))
        return max(p)
