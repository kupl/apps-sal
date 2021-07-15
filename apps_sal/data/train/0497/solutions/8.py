class Solution:
    def binsearch(self, arr, ele, l, r):
        while (r-l>1):
            mid = l + (r-l)//2 
            if arr[mid][1]==ele:
                return mid
            elif arr[mid][1]>ele:
                r=mid 
            else: 
                l=mid 
            
        return(l)
                
        
        
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n=len(startTime)
        dp=[0]*n
        times = []
        for i in range(n):
            times.append([startTime[i], endTime[i], profit[i]])
            
        
        times.sort(key = lambda it:it[1])
        #print(times)
        
        dp[0]=times[0][2]
        
        for i in range(1,n):
            prof = times[i][2]
            binInd = self.binsearch(times, times[i][0], -1, i)
            #print(binInd)
            if binInd!=-1:
                prof+=dp[binInd]
            
            dp[i]=max(dp[i-1], prof)
        
        return dp[n-1]
        
        
        
        

