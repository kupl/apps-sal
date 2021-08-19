class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l = len(nums)
        return (nums[l - 1] - 1) * (nums[l - 2] - 1)
