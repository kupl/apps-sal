class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        flag = [0]*n
        i = 0
        
        while i<n:
            j = i+1
            while j<n:
                if flag[i]!=1:
                    print((i,j,intervals[i], intervals[j]))
                    if intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]:
                        flag[i] = 1
                    if intervals[i][0] <= intervals[j][0] and intervals[j][1] <= intervals[i][1]:
                        flag[j] = 1
                j+=1  
            i+=1                
                

        return flag.count(0)
            

