class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        highest = max(nums)
        nums.pop(nums.index(max(nums)))
        second_highest = max(nums)
        return (highest - 1) * (second_highest - 1)
