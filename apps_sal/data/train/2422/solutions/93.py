class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        list1 = [((nums[i]-1)*(nums[j]-1)) for i in range(len(nums)) for j in range(i+1,len(nums))]
        return max(list1)

