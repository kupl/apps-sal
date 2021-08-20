class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        return self.m1_sort(intervals)

    def m1_sort(self, intervals):
        intervals.sort(key=lambda x: x[1], reverse=True)
        intervals.sort(key=lambda x: x[0])
        count = 0
        max_end = 0
        for interval in intervals:
            if interval[1] > max_end:
                max_end = interval[1]
                count += 1
        return count
