class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],-x[1]))
        ub = [x[1] for x in intervals]
        d = [(x - max(ub[:i+1]))<=0 for i,x in enumerate(ub[1:])]
        return len(intervals)-sum(d)
