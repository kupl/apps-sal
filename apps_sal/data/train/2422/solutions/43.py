class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        s = sorted(nums, reverse=True)
        return (s[0] - 1) * (s[1] - 1)
