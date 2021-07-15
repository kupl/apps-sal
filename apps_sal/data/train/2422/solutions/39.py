class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i,v in enumerate(nums):
            nums[i]=nums[i]-1
            nums[i]=abs(nums[i])
        nums.sort(reverse=True)
        return (nums[0])*(nums[1])
