class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        removeSet = set()
        for i in range(n):
            interval1 = intervals[i]
            for j in range(i + 1, n):
                interval2 = intervals[j]
                if interval2[0] >= interval1[1]:
                    break
                if interval2[1] <= interval1[1]:
                    removeSet.add(j)
        return n - len(removeSet)
