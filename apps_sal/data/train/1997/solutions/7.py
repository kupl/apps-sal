import numpy as np


class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        copy_intervals = intervals[:]
        for (i, interval_1) in enumerate(copy_intervals):
            for interval_2 in copy_intervals[i + 1:]:
                if interval_1[0] >= interval_2[0] and interval_1[1] <= interval_2[1]:
                    if interval_1 in intervals:
                        intervals.remove(interval_1)
                    break
                if interval_1[0] <= interval_2[0] and interval_1[1] >= interval_2[1]:
                    if interval_2 in intervals:
                        intervals.remove(interval_2)
        return len(intervals)
