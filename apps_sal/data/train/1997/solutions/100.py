class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        new_intervals = []
        new_intervals.append(sorted_intervals[0])
        for i in sorted_intervals:
            n = new_intervals[-1]
            if i[0] >= n[0] and i[1] <= n[1]:
                continue
            new_intervals.append(i)
        return len(new_intervals)
