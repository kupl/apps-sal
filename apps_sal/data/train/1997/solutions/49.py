class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        flags=[]
        for i in range(n):
            flags.append(0)
        k=n
        for i in range(n):
            for j in range(n):
                if(i==j or flags[j]==1):
                    continue
                if(intervals[i][0]<=intervals[j][0] and intervals[i][1]>=intervals[j][1]):
                    flags[j]=1
                    k-=1
        return k
                    
        

