class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        max1 = nums.pop(nums.index(max(nums)))
        max2 = nums.pop(nums.index(max(nums)))
        return (max1 - 1) * (max2 - 1)
