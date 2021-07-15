class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        covering = 0
        used = set()
        for i, (si, ei) in enumerate(intervals):
            for sj, ej in intervals[i+1:]:                
                if sj > ei:
                    break
                if ej > ei:
                    continue
                if (sj, ej) in used:
                    continue
                used.add((sj, ej))
                covering += 1
                
        return len(intervals) - covering
            

