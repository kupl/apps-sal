class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n_intervals = len(intervals)
        if intervals:
            intervals = sorted(intervals, key=lambda x: x[0] - x[1])
            i = len(intervals) - 1
            while i > 0:
                interval_i = intervals[i]
                j = i - 1
                while j >= 0:
                    if intervals[j][0] <= interval_i[0] and intervals[j][1] >= interval_i[1]:
                        n_intervals -= 1
                        break
                    j -= 1
                i -= 1
        return n_intervals
