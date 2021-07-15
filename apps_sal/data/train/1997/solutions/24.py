class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda k: (k[0], -k[1]))
        removed = set()
        i = 0
        while i < len(intervals) - 1:
            for j in range(i + 1, len(intervals)):
                if intervals[j][1] <= intervals[i][1] and j not in removed:
                    removed.add(j)
            i += 1
        return len(intervals) - len(removed)
