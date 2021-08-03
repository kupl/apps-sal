class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        removed=[False for _ in range(len(intervals))]
        
        
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if removed[j] or i==j:
                    continue
                    
                if intervals[i][0] <= intervals[j][0] and intervals[j][0] <= intervals[i][1] and \\
                    intervals[i][0] <= intervals[j][1] and intervals[j][1] <= intervals[i][1]:
                    removed[j]=True
                    
        return removed.count(False)
        
