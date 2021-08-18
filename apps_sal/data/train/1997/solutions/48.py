class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        removed = [False] * n
        intervals = sorted(intervals, key=lambda interval: (interval[0], -interval[1]))
        for i in range(len(intervals)):
            start, end = intervals[i]
            j = i + 1
            while j < len(intervals) and end >= intervals[j][0]:
                if end >= intervals[j][1] and not removed[j]:
                    removed[j] = True
                    n -= 1
                j += 1

        return n
