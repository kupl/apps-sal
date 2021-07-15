class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        removed = 0
        removed_list = {}
        
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                if i in removed_list or j in removed_list:
                    continue
                elif (intervals[j][0] <= intervals[i][0] <= intervals[j][1] and intervals[j][0] <= intervals[i][1] <= intervals[j][1]):
                    removed_list[i] = True    
                    removed += 1                
                elif (intervals[i][0] <= intervals[j][0] <= intervals[i][1] and intervals[i][0] <= intervals[j][1] <= intervals[i][1]):
                    removed_list[j] = True
                    removed += 1
        
        return len(intervals) - removed
                

