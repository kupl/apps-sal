class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        l = len(intervals)
        a = [True] * l

        for i in range(l):
            for j in range(l):
                if i == j:
                    continue

                if not a[i] or not a[j]:
                    continue

                if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                    a[j] = False

        return a.count(True)
