class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = len(intervals)
        for i in range(len(intervals)):
            for j in range(len(intervals)):                
                if((i!=j) & (intervals[i][0] >= intervals[j][0]) & (intervals[i][1] <= intervals[j][1])): 
                    count=count-1
                    break
        return count
