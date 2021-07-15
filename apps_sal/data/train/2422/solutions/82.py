class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if ans<(nums[i]-1)*(nums[j]-1):
                    ans=(nums[i]-1)*(nums[j]-1)
        return ans
            

