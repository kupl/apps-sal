class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def isCovered(interval, candidates):
            for c in candidates:
                if c[0] <= interval[0] and c[1] >= interval[1]:
                    return True
            return False
        
        cnt = 0
        for i, interval in enumerate(intervals):
            if not isCovered(interval, intervals[:i]+intervals[i+1:]):
                cnt += 1
        return cnt
