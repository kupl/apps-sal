from collections import defaultdict

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = max(endTime)
        lookup = defaultdict(list)
        for s,e,p in zip(startTime,endTime,profit): lookup[e].append((s,p))
        dp = [0]*(n+1)
        
        for i in range(1,len(dp)):
            dp[i] = dp[i-1]
            if i in lookup:
                for start,prof in lookup[i]:
                    dp[i] = max(dp[i],dp[start]+prof)
        return dp[-1]
        
        
    '''
    [[1,3],[2,4],[3,5],[3,6]] [50,10,40,70]
    
    [0,-i,-i,50,50,90,120]
    
    startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
    [0,0,0,20,20,20,90,90,90,150,150]
    
    [1,2,3,3]
    [3,4,5,6]
    [50,10,40,70]
  [0,0,0,50,50,90,120] 
    dp = []
    
    
    [47,13,28,16,2,11]
    [48,35,48,26,21,39]
    [11,13,2,15,1,1]
    
    [1,15,15,15,17]
    '''

