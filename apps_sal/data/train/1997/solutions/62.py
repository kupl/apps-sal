class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        k=0
        for i in range(len(intervals)):
            for j in range(0,len(intervals)):
                if i==j:
                    continue
                if (intervals[i][0]>=intervals[j][0]) and intervals[i][1]<=intervals[j][1]:
                    k+=1
                    break
        return len(intervals)-k
        

