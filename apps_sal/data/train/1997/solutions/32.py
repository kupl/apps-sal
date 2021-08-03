import numpy as np


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        current_intervals = np.array(intervals)

        for interval in intervals:
            mask = np.logical_and(current_intervals[:, 0] >= interval[0], current_intervals[:, 1] <= interval[1])
            current_intervals = current_intervals[np.logical_not(mask)]
            if sum(mask):
                current_intervals = np.append(current_intervals, [interval], axis=0)

        return len(current_intervals)
