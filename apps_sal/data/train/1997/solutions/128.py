class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        i = 1
        while i < len(intervals):
            a = intervals[i][0]
            b = intervals[i][1]
            c = intervals[i - 1][0]
            d = intervals[i - 1][1]
            if c <= a and d >= b:
                intervals.pop(i)
            else:
                i += 1
        i = len(intervals) - 2
        print(i)
        print((len(intervals)))
        while i >= 0:
            a = intervals[i][0]
            b = intervals[i][1]
            c = intervals[i + 1][0]
            d = intervals[i + 1][1]
            if c <= a and d >= b:
                intervals.pop(i)
                i -= 1
            else:
                i -= 1
        return len(intervals)
