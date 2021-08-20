class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        i = 0
        while i < len(intervals):
            for k in intervals:
                if intervals[i][0] >= k[0] and intervals[i][1] <= k[1]:
                    if intervals[i] != k:
                        intervals.pop(i)
                        if i > 0:
                            i = i - 1
            i = i + 1
        return len(intervals)
