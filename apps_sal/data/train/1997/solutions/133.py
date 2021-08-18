class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        i = 0
        while i < len(intervals):
            j = i + 1
            while j < len(intervals):
                if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                    intervals.pop(j)
                    j = i + 1
                elif intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                    intervals.pop(i)
                    j = i + 1
                else:
                    j = j + 1
            i = i + 1
        return len(intervals)
