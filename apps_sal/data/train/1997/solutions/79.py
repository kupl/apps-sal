class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        op = 0
        if len(intervals) < 2:
            return len(intervals)
        for j in intervals:
            for k in intervals:
                if j[0] != k[0] or j[1] != k[1]:
                    if j[0] >= k[0] and j[1] <= k[1]:
                        op += 1
                        break
        return len(intervals) - op
