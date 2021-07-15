class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                s=(nums[i]-1)*(nums[j]-1)
                l.append(s)
        return max(l)
                

