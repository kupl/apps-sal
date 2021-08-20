class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        def overlap(interval1, interval2):
            if interval1[0] > interval2[0]:
                (interval1, interval2) = (interval2, interval1)
            return interval1[1] >= interval2[1]
        intervals.sort(key=lambda x: (x[0], -x[1]))
        print(intervals)
        count = 0
        res = [intervals[0]]
        for i in intervals[1:]:
            print((i, res[-1]))
            if not overlap(res[-1], i):
                res.append(i)
        return len(res)
