class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return max((nums[i]-1)*(nums[j]-1) for i in range(len(nums)) for j in range(i+1, len(nums)))
