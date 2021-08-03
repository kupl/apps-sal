class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        length = len(intervals)
        start = 0
        removed = 0

        while start < length - 1:
            curr = start + 1
            while curr < length:
                if intervals[curr][0] != -1:
                    if (intervals[curr])[0] >= (intervals[start])[0] and (intervals[curr])[1] <= (intervals[start])[1]:
                        removed += 1
                        (intervals[curr])[0] = -1
                        (intervals[curr])[1] = -1
                curr += 1
            start += 1
        return length - removed
