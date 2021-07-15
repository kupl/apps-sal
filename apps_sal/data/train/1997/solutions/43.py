class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        drop = set([])
        for i in range(len(intervals)):
            x, y = intervals[i]
            for j in range(i+1, len(intervals)):
                a, b = intervals[j]
                
                if x >= a and y <= b:
                    drop.add(i)
                    break
                elif a >= x and b <= y:
                    drop.add(j)
                    
        return len(intervals)-len(drop)
