class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                ans = max((nums[i] - 1) * (nums[j] - 1), ans)
        return ans
