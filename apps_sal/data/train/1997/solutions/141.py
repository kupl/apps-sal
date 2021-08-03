class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        res = n
        for i in range(n - 1):
            for j in range(i + 1, n):
                if intervals[i][0] < 0 or intervals[j][0] < 0:
                    continue
                if (intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]):
                    intervals[j][0] = -1
                    res -= 1
                    continue
                elif (intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]):
                    res -= 1
                    intervals[i][0] = -1
                    break
        return res
