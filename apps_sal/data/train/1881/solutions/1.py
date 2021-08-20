class Solution:

    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        r1 = [x[0] for x in intervals]
        r2 = [x[1] for x in intervals]
        intervals = sorted(intervals, key=lambda x: x[1])
        s = [intervals[0][1] - 1, intervals[0][1]]
        for interval in intervals:
            if interval[0] > s[-1]:
                s += [interval[1] - 1, interval[1]]
            elif interval[0] > s[-2]:
                s += [interval[1]]
        return len(s)
