class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx=float('-inf')
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if maxx<(nums[i]-1)*(nums[j]-1):
                    maxx=(nums[i]-1)*(nums[j]-1)
        return maxx

