class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq=[0]*len(nums)
        for a,b in requests:
            freq[a]+=1
            if b+1<len(nums): freq[b+1]-=1
        for i in range(1,len(nums)):
            freq[i]+=freq[i-1]
            
        freq.sort()
        nums.sort()
        ans=0
        for i in range(len(nums)):
            ans=(ans+freq[i]*nums[i])%((10**9)+7)
        return ans

