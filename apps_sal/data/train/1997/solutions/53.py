class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        s = set()
        for i, [a,b] in enumerate(intervals):
            for j, [c,d] in enumerate(intervals[i+1:]):
                if (c <= a and b <= d):
                    s.add((a,b))
                elif (a <= c and d <= b):
                    s.add((c,d))
        return len(intervals) - len(s)
