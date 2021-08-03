class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        l = len(intervals)
        removed = set()
        intervals.sort(key=lambda i: (i[0], -i[1]))
        for i in range(l):
            for j in range(i + 1, l):
                if intervals[i][1] >= intervals[j][1]:
                    removed.add(j)
        return l - len(removed)
