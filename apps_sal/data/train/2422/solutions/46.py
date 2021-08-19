class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        Max = max(nums)
        nums.remove(Max)
        return (Max - 1) * (max(nums) - 1)
