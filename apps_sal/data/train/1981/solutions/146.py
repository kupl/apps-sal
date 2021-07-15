class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        nums.sort(reverse=True)
        
        index=[0]*len(nums)
        for start,end in requests:
            index[start]+=1
            if (end+1)<len(nums):
                index[end+1]-=1
            
        for i in range(1,len(nums)):
            index[i]+=index[i-1]
        
        
        index.sort(reverse=True)
        
        result=0
        for i in range(len(index)):
            freq=index[i]
            value=nums[i]
            
            if freq==0:
                break
            result+=value*freq
            
        return result%(10**9+7)

