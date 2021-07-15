class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        ans=float('-inf')
        for i in range(n-1):
            for j in range(i+1,n):
                ans=max((nums[i]-1)*(nums[j]-1),ans)
        return ans

