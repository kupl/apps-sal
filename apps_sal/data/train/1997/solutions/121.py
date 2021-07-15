class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        count = length = len(intervals)
        removedIdx = set()
        for i in range(length-1):
            for j in range(i+1, length):
                if i in removedIdx or j in removedIdx:
                    continue
                a, b = intervals[i][0], intervals[i][1]
                c, d = intervals[j][0], intervals[j][1]
                
                if a <= c and b >= d:
                    count -= 1
                    removedIdx.add(j)
                elif c <= a and d >= b:
                    count -= 1
                    removedIdx.add(i)

                    
        return count
