class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1] - interval[0])
        # print(intervals)
        counter = 0
        i = 0
        n = len(intervals)
        for i in range(n):
            covered = False
            for j in range(i+1, n):
                if self.cover(intervals[j], intervals[i]):
                    covered = True
                    break
            if not covered:
                counter += 1
        return counter
                
            
        
    def cover(self, interval1, interval2):
        # return whether interval1 cover interval2
        return interval1[0] <= interval2[0] and interval1[1] >= interval2[1] 

