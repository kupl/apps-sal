class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        for i in range(n):
            for j in range(i + 1, n):
                if intervals[i][0] > intervals[j][0]:
                    intervals[i], intervals[j] = intervals[j], intervals[i]
        l = [intervals[0]]
        for i in range(1, n):
            if (intervals[i][0] >= l[-1][0] and intervals[i][1] <= l[-1][1]):
                intervals[i] = -1
            elif(intervals[i][0] <= l[-1][0] and intervals[i][1] >= l[-1][1]):
                intervals[i - 1] = -1
            if intervals[i] != -1:
                l.append(intervals[i])
        print(intervals)
        return n - intervals.count(-1)
