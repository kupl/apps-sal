class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i != j:
                    if intervals[i] != 0 and intervals[j] != 0:
                        if intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]:
                            intervals[i] = 0
        c = 0
        for i in intervals:
            if i != 0:
                c += 1
        return c
