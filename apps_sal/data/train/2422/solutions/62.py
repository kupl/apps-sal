class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        return (sorted_nums[-1] - 1) * (sorted_nums[-2] - 1)
