class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals,key=lambda x:x[1])
        n=len(intervals)
        cnt=0
        for i in intervals:
            for j in intervals:
                if j==i:
                    continue
                if i[1]<=j[1] and i[0]>=j[0]:
                    cnt+=1
                    break
        return(n-cnt)
                    
        

