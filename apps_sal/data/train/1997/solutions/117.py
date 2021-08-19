class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        len_interval = len(intervals)
        if len_interval == 1:
            return 1
        count = len_interval
        for i in range(len_interval):
            part_intervals = intervals[:i] + intervals[i + 1:]
            for interval in part_intervals:
                if self.isOverlapping(intervals[i], interval):
                    count -= 1
                    break
        return count

    def isOverlapping(self, interval_1: List[int], interval_2: List[int]) -> bool:
        if interval_2[0] <= interval_1[0] and interval_1[1] <= interval_2[1]:
            return True
        else:
            return False
