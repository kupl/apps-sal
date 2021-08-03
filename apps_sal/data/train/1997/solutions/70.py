class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        ref = [1] * n

        for i in range(n):
            for j in range(n):
                if i == j or not (ref[i] & ref[j]):
                    continue

                if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                    ref[j] = 0
        return sum(ref)
