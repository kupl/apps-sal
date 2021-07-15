class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        
        
        for i in range(len(intervals)-1):
            
            if(intervals[i][0]==-1):
                continue
            
            
            for j in range(i+1,len(intervals)):
                t=intervals[i]
                tn=intervals[j]
                
                
                if(t[0]<=tn[0] and tn[1]<=t[1]):
                    intervals[j][0],intervals[j][1]=-1,-1
            
                elif(tn[0]<=t[0] and t[1]<=tn[1]):
                    intervals[i][0],intervals[i][1]=-1,-1
                    
        
        count=0
        
        for i in intervals:
            if(i[0]!=-1):
                count+=1
        
        return(count)
