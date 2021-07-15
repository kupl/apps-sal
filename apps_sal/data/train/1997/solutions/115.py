class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        l = intervals[:]
        
        for i in range(len(intervals)):
            flag = 0
            for j in range(len(intervals)):
                if i!=j:
                    if intervals[i][0] in range(intervals[j][0],intervals[j][1]+1) and intervals[i][1] in range(intervals[j][0],intervals[j][1]+1):
                        flag = 1
                        l.remove(intervals[i])
                        break
                if flag==1:
                    break
        return len(l)
