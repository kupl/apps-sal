class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = max(nums)
        nums.remove(a)
        return (a-1)*(max(nums)-1)

