class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        i = 0
        j = 1
        while i < len(intervals) and j < len(intervals):
            if intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:

                intervals.pop(i)
                i, j = 0, 1
            elif intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                intervals.pop(j)
                i, j = 0, 1
            else:
                j += 1

            if j == len(intervals):
                i += 1
                j = i + 1

        return len(intervals)
