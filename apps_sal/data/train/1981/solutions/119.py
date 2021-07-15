class Solution:
    
    def update(self,d,s,e):
        d[s]+=1
        d[e+1]-=1
        
        
        
        
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        n=len(nums)
        d=[0]*(n+1)
        m=10**9+7
        for i in range(len(requests)):
            s=requests[i][0]
            e=requests[i][1]
            self.update(d,s,e)
                
     

        for i in range(0,n):
            if i==0:
                continue
            else:
                d[i]=d[i]+d[i-1]
                
        d.pop()
                
        d.sort()
        
        count=0
        for i in range(n):
            count=(count+d[i]*nums[i])%m
            
        return count%m
        
        

